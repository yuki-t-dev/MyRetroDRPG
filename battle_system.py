import pyxel

from constants import TILE_SIZE

class BattleSystem:
    def __init__(self, game):
        self.game = game
        self.game.party.members[0].take_damage(10)

    def draw_battle(self):
        pyxel.cls(0)
        pyxel.text(10, 30, "Battle Scene - Press A to return", pyxel.COLOR_WHITE)

    def show_status(self, x, y, member):
        pyxel.blt(x, y, member.img, 0, 0, TILE_SIZE, TILE_SIZE, pyxel.COLOR_PURPLE)
        pyxel.text(x+20, y, f":{member.name}", self.decide_color(member))
        pyxel.text(x, y+20, f"HP:{member.hp}/{member.max_hp} MP:{member.mp}/{member.max_mp}", self.decide_color(member))
        pyxel.rectb(x-3, y-3, 80, 30, self.decide_color(member))

    def draw_allys(self):
        for i, member in enumerate(self.game.party.members):
            x = 5 + i * 80 
            y = 200
            self.show_status(x, y, member)

    def decide_color(self, member):
        if member.hp <= 0:
            return pyxel.COLOR_RED
        elif member.hp <= member.max_hp * 0.3:
            return pyxel.COLOR_YELLOW
        else:
            return pyxel.COLOR_WHITE