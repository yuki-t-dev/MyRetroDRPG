import pyxel
import random

from constants import TILE_SIZE, MINIMAP_TILE_SIZE

class Dungeon:
    TILE_WALL = 0
    TILE_FLOOR = 1

    def __init__(self, game, w, h):
        self.game = game
        self.w = w
        self.h = h
        self.radius = 6
        self.view_w = self.radius * 2 + 1
        self.view_h = self.radius * 2 + 1

        self.currnet_floor = 1

        self.cam_x = 0
        self.cam_y = 0

        self.cam_px = 0
        self.cam_py = 0

        self.wall_img = pyxel.Image(16, 16)
        self.field_img = pyxel.Image(16, 16)
        self.stairs_img = pyxel.Image(16, 16)

        self.wall_img.load(0, 0, "assets/wall.png",)
        self.field_img.load(0, 0, "assets/field.png",)
        self.stairs_img.load(0, 0, "assets/stairs.png",)

        self.reset()
        self.generate()

    def reset(self):
        self.map = [[self.TILE_WALL for _ in range(self.w)] for _ in range(self.h)]
        self.rooms = []

        self.visible = [[False for _ in range(self.w)] for _ in range(self.h)]
        self.explored = [[False for _ in range(self.w)] for _ in range(self.h)]

    def generate(self, room_count=14):
        self.reset()
        self.generate_maze()
        self.add_rooms(room_count)
        self.connect_rooms()
        self.clean_isolated()
    
    def generate_maze(self):
        stack = [(1, 1)]
        self.map[1][1] = self.TILE_FLOOR
        while stack:
            x, y = stack[-1]
            dirs = [(2,0),(-2,0),(0,2),(0,-2)]
            random.shuffle(dirs)

            carved = False
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.w-1 and 1 <= ny < self.h-1:
                    if self.map[ny][nx] == self.TILE_WALL:
                        self.map[y + dy//2][x + dx//2] = self.TILE_FLOOR
                        self.map[ny][nx] = self.TILE_FLOOR
                        stack.append((nx, ny))
                        carved = True
                        break
            if not carved:
                stack.pop()
    
    def is_overlapping(self, x, y, w, h, margin=1):
        for rx, ry, rw, rh in self.rooms:
            if (x < rx + rw + margin and
                x + w + margin > rx and
                y < ry + rh + margin and
                y + h + margin > ry):
                return True
        return False

    def add_rooms(self, count):
        attemps = 0
        max_attempts = count * 10

        while len(self.rooms) < count and attemps < max_attempts:
            attemps += 1

            rw = random.randint(4, 8)
            rh = random.randint(4, 8)
            rx = random.randint(1, self.w - rw - 2)
            ry = random.randint(1, self.h - rh - 2)

            if self.is_overlapping(rx, ry, rw, rh):
                continue

            for y in range(ry, ry + rh):
                for x in range(rx, rx + rw):
                    self.map[y][x] = self.TILE_FLOOR
            
            self.rooms.append((rx, ry, rw, rh))

            cx = rx + rw //2
            cy = ry + rh //2
            self.connect_to_maze(cx, cy)

    def connect_to_maze(self, x, y):
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            for i in range(1, 15):
                nx = x + dx*i
                ny = y + dy*i
                if not (0 <= nx < self.w and 0 <= ny < self.h):
                    break
                if self.map[ny][nx] == self.TILE_FLOOR:
                    for j in range(i):
                        self.map[y + dy*j][x + dx*j] = self.TILE_FLOOR
                    return

    def connect_rooms(self):
        for i in range(len(self.rooms) -1):
            x1, y1, w1, h1 = self.rooms[i]
            x2, y2, w2, h2 = self.rooms[i+1]

            cx1, cy1 = x1 + w1//2, y1 + h1//2
            cx2, cy2 = x2 + w2//2, y2 + h2//2

            if random.random() < 0.5:
                self.h_corridor(cx1, cx2, cy1)
                self.v_corridor(cy1, cy2, cx2)
            else:
                self.v_corridor(cy1, cy2, cx1)
                self.h_corridor(cx1, cx2, cy2)

    def h_corridor(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[y][x] = self.TILE_FLOOR

    def v_corridor(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[y][x] = self.TILE_FLOOR

    def clean_isolated(self):
        for y in range(1, self.h-1):
            for x in range(1, self.w-1):
                if self.map[y][x] == self.TILE_FLOOR:
                    count = 0
                    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        if self.map[y + dy][x + dx] == self.TILE_FLOOR:
                            count += 1
                    if count <= 1:
                        self.map[y][x] = self.TILE_WALL

    def get_random_floor(self):
        while True:
            x = random.randint(1, self.w - 2)
            y = random.randint(1, self.h - 2)
            for rx, ry, rw, rh in self.rooms:
                if self.map[y][x] == self.TILE_FLOOR and (rx, ry) == (x, y):
                    return x, y

    def spawn_goal(self):
        if not self.currnet_floor == 1:
            self.game.player.grid_x, self.game.player.grid_y = self.get_random_floor()
        while True:
            self.goal_x, self.goal_y = self.get_random_floor()
            if (self.goal_x, self.goal_y) != (self.game.player.grid_x, self.game.player.grid_y):
                break

    def update_fov(self, px, py, radius=6):
        for y in range(self.h):
            for x in range(self.w):
                dx = x - px
                dy = y - py
                dist = dx*dx + dy*dy

                if dist <= radius**2:
                    self.visible[y][x] = True
                    self.explored[y][x] = True
                else:
                    self.visible[y][x] = False

    def update(self):
        self.update_fov(self.game.player.grid_x, self.game.player.grid_y, radius=self.radius)
        if (self.game.player.grid_x, self.game.player.grid_y) == (self.goal_x, self.goal_y):
            self.currnet_floor += 1
            self.generate()
            self.spawn_goal()
            self.game.scenes["play"].initialized = False

    def draw(self):
        pyxel.cls(0)

        target_x = self.game.player.px - (self.view_w * TILE_SIZE) // 2
        target_y = self.game.player.py - (self.view_h * TILE_SIZE) // 2

        self.cam_px += (target_x - self.cam_px) * 0.2
        self.cam_py += (target_y - self.cam_py) * 0.2

        max_x = self.w * TILE_SIZE - self.view_w * TILE_SIZE 
        max_y = self.h * TILE_SIZE - self.view_h * TILE_SIZE

        self.cam_px = max(0, min(self.cam_px, max_x))
        self.cam_py = max(0, min(self.cam_py, max_y))

        self.cam_x = int(self.cam_px // TILE_SIZE)
        self.cam_y = int(self.cam_py // TILE_SIZE)


        for sy in range(self.view_h + 1):
            for sx in range(self.view_w + 1):
                mx = int(self.cam_px // TILE_SIZE) + sx
                my = int(self.cam_py // TILE_SIZE) + sy

                if not (0 <= mx < self.w and 0 <= my < self.h):
                    continue

                draw_x = int(sx * TILE_SIZE - (self.cam_px % TILE_SIZE))
                draw_y = int(sy * TILE_SIZE - (self.cam_py % TILE_SIZE))

                if not self.explored[my][mx]:
                    col = 0
                    pyxel.rect(draw_x, draw_y, TILE_SIZE, TILE_SIZE, col)
                elif not self.visible[my][mx]:
                    continue
                else:

                    pyxel.blt(draw_x, draw_y, self.field_img if self.map[my][mx] == self.TILE_FLOOR else self.wall_img, 0, 0, TILE_SIZE, TILE_SIZE)

        if self.visible[self.goal_y][self.goal_x] and self.explored[self.goal_y][self.goal_x]:
            gx = int(self.goal_x * TILE_SIZE - self.cam_px)
            gy = int(self.goal_y * TILE_SIZE - self.cam_py)
            #pyxel.rect(gx, gy, TILE_SIZE, TILE_SIZE, 11)
            pyxel.blt(gx, gy, self.stairs_img, 0, 0, self.stairs_img.width, self.stairs_img.height, pyxel.COLOR_PURPLE)

        offset_x = (self.view_w + 2) * TILE_SIZE
        offset_y = TILE_SIZE

        pyxel.rectb(offset_x-1, offset_y-1, self.w * MINIMAP_TILE_SIZE + 2, self.h * MINIMAP_TILE_SIZE + 2, 7)

        for y in range(self.h):
            for x in range(self.w):
                if not self.explored[y][x]:
                    continue
                col = 1 if self.map[y][x] == self.TILE_WALL else pyxel.COLOR_WHITE
                px = offset_x + x * MINIMAP_TILE_SIZE
                py = offset_y + y * MINIMAP_TILE_SIZE
                pyxel.rect(px, py, MINIMAP_TILE_SIZE, MINIMAP_TILE_SIZE, col)
        
        cam_px = offset_x + self.cam_x * MINIMAP_TILE_SIZE
        cam_py = offset_y + self.cam_y * MINIMAP_TILE_SIZE

        cam_w = self.view_w * MINIMAP_TILE_SIZE
        cam_h = self.view_h * MINIMAP_TILE_SIZE

        pyxel.rectb(cam_px, cam_py, cam_w, cam_h, 8)

        px = offset_x + self.game.player.grid_x * MINIMAP_TILE_SIZE
        py = offset_y + self.game.player.grid_y * MINIMAP_TILE_SIZE
        pyxel.rect(px, py, MINIMAP_TILE_SIZE, MINIMAP_TILE_SIZE, pyxel.COLOR_RED)

        if self.explored[self.goal_y][self.goal_x]:
            gx = offset_x + self.goal_x * MINIMAP_TILE_SIZE
            gy = offset_y + self.goal_y * MINIMAP_TILE_SIZE
            pyxel.rect(gx, gy, MINIMAP_TILE_SIZE, MINIMAP_TILE_SIZE, 11)
