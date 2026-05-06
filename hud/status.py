import pyxel

from constants import TILE_SIZE, VIEW_WIDTH
from utility import draw_text, decide_color_from_hp

class ViewStatus:
    def __init__(self, game):
        self.game = game
        self.font10 = pyxel.Font("assets/umplus_j10r.bdf")

    def draw_floor(self):
        draw_text(TILE_SIZE*(VIEW_WIDTH+2.1), 2, f"Floor:{self.game.dungeon.current_floor}", pyxel.COLOR_WHITE, style="shadow")

    def show_status(self, x, y, member):
        pyxel.blt(x, y, member.img, 0, 0, TILE_SIZE, TILE_SIZE, pyxel.COLOR_PURPLE)
        draw_text(x+20, y-2, f"{member.name}", decide_color_from_hp(member), style="shadow")
        draw_text(x+20, y+10, f"HP:{member.hp}/{member.max_hp}", decide_color_from_hp(member), style="shadow")
        draw_text(x+20, y+20, f"MP:{member.mp}/{member.max_mp}", decide_color_from_hp(member), style="shadow")
        pyxel.rectb(x-3, y-3, 85, 35, decide_color_from_hp(member))

    def draw_allys(self):
        for i, member in enumerate(self.game.party.battle_party):
            x = TILE_SIZE*(VIEW_WIDTH+2)
            y = 90 + i * 38
            self.show_status(x, y, member)

