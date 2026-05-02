import pyxel

from sound import BattleBGM

class BattleScene:
    def __init__(self, game):
        self.game = game
        self.battle_bgm = BattleBGM()
    def start(self):
        game = self.game
        self.battle_bgm.play()

    def update(self):
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
            self.game.change_scene("play")

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10,10,self.__class__.__name__,1)
        self.game.draw_battle()