#import pyxel

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
        self.game.battle.update_battle()

    def draw(self):
        self.game.draw_battle()