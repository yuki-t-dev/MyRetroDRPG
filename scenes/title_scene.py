import pyxel

from sound import TitleBGM

class TitleScene:
    def __init__(self, game):
        self.game = game
        self.title_bgm = TitleBGM()
        self.opening_img = pyxel.Image(324, 240)
        self.opening_img.load(0, 0, "assets/opening.png")

        self.se_pressed = pyxel.Sound()
        self.se_pressed.mml("t120 o5 v10 l16 g >C")

        self.fire = FireEffect()
        self.star = Star()

    def start(self):
        self.game.current_floor = 1
        self.title_bgm.play()

    def update(self):
        if  pyxel.btnp(pyxel.KEY_RETURN) or\
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B) or\
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A) or\
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START) or\
            pyxel.btnp(pyxel.GAMEPAD1_BUTTON_GUIDE) or\
            pyxel.btnp(pyxel.KEY_LEFT) or\
            pyxel.btnp(pyxel.KEY_RIGHT) or\
            pyxel.btnp(pyxel.KEY_UP) or\
            pyxel.btnp(pyxel.KEY_DOWN):
            pyxel.play(0, self.se_pressed)
            self.game.change_scene("opening")

        self.fire.update()
        self.star.update()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, self.opening_img, 0, 0, self.opening_img.width, self.opening_img.height)

        self.fire.draw()
        self.star.draw()

class FireEffect:
    def __init__(self):
        self.col1 = self.col2 = 4
    def update(self):
        if pyxel.frame_count % 6 == 0:
            self.col1 = 4
        else:
            self.col1 = 9

        if pyxel.frame_count % 8 == 0:
            self.col2 = 4
        else:
            self.col2 = 9
    def draw(self):
        pyxel.rect(234, 136, 2, 2, self.col1)
        pyxel.rect(264, 136, 2, 2, self.col2)

class Star:
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.vx = 5 
        self.vy = 3
        self.trail = []
        self.alive = True
        self.wait = pyxel.rndi(30, 120)

    def update(self):
        if self.wait > 0:
            self.wait -= 1
            return
        if not self.alive:
            return
        self.x += self.vx
        self.y += self.vy

        self.trail.append((self.x, self.y))
        if len(self.trail) > 10:
            self.trail.pop(0)
        if self.x>200:
            self.alive = False

    def draw(self):
        if not self.alive:
            return
        for i, (x, y) in enumerate(self.trail):
            col = 7 - i // 2  # 徐々に暗く
            pyxel.pset(x, y, max(col, 1))

        pyxel.pset(self.x, self.y, 7)
