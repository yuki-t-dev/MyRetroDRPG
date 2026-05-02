import pyxel

class BattleSystem:
    def __init__(self, game):
        self.game = game
        self.game.party.members[0].take_damage(10)

    def draw_battle(self):
        pyxel.cls(0)
        pyxel.text(10, 30, "Battle Scene - Press A to return", pyxel.COLOR_WHITE)