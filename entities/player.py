import pyxel

from constants import TILE_SIZE

class Player:
    def __init__(self, game, x, y):
        self.game = game

        self.grid_x = x
        self.grid_y = y

        self.px = x * TILE_SIZE 
        self.py = y * TILE_SIZE

        self.moving = False
        self.target_x = self.px
        self.target_y = self.py
        self.speed = 4

        self.player_img = pyxel.Image(16, 16)
        #self.player_img.load(0, 0, "assets/player.png")

    def try_move(self, dx, dy):
        if self.moving:
            return

        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        if self.game.dungeon.map[new_y][new_x] == self.game.dungeon.TILE_FLOOR:
            self.grid_x = new_x
            self.grid_y = new_y

            self.target_x = self.grid_x * TILE_SIZE
            self.target_y = self.grid_y * TILE_SIZE

            self.moving = True

    def update(self):
        moved = False

        if not self.moving:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.try_move(-1, 0)
            elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.try_move(1, 0)
            elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                self.try_move(0, -1)
            elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                self.try_move(0, 1)

        if self.moving:
            self.px += (self.target_x - self.px) * 0.4
            self.py += (self.target_y - self.py) * 0.4

            if abs(self.px - self.target_x) < 0.5 and abs(self.py - self.target_y) < 0.5:
                self.px = self.target_x
                self.py = self.target_y
                self.moving = False
                moved = True
        
        return moved

    def draw(self):
        sx = int(self.game.player.px - self.game.dungeon.cam_px)
        sy = int(self.game.player.py - self.game.dungeon.cam_py)
        member = self.game.party.alive_members()[0]
        self.player_img.load(0, 0, f"assets/{member.file_path}")
        pyxel.blt(sx, sy, self.player_img, 0, 0, self.player_img.width, self.player_img.height, pyxel.COLOR_PURPLE)