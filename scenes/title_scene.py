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

    def start(self):
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
            self.game.change_scene("play")

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, self.opening_img, 0, 0, self.opening_img.width, self.opening_img.height)

