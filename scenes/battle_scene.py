import pyxel

from sound import BattleBGM
from battle_system import BattleSystem

class BattleScene:
    def __init__(self, game):
        self.game = game
        self.battle_bgm = BattleBGM()
    def start(self):
        game = self.game
        game.battle = BattleSystem(game)
        self.battle_bgm.play()

    def update(self):
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_A):
            self.game.change_scene("play")

    def draw(self):
        self.game.draw_battle()