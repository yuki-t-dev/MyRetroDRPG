import pyxel

from constants import TILE_SIZE, VIEW_WIDTH

class ViewStatus:
    def __init__(self, game):
        self.game = game

        self.hero_img = pyxel.Image(16, 16)
        self.hero_img.load(0, 0, "assets/player.png")

        self.heroine_img = pyxel.Image(16, 16)
        self.heroine_img.load(0, 0, "assets/heroine.png")

        self.blackmaze_img = pyxel.Image(16, 16)
        self.blackmaze_img.load(0, 0, "assets/blackmaze.png")

        self.wildhero_img = pyxel.Image(16, 16)
        self.wildhero_img.load(0, 0, "assets/wildhero.png")

    def draw_floor(self):
        pyxel.text(TILE_SIZE*(VIEW_WIDTH+1), 5, f"Floor: {self.game.dungeon.currnet_floor}", pyxel.COLOR_WHITE)

    def draw_allys(self):
        pyxel.blt(TILE_SIZE*(VIEW_WIDTH+2), 100, self.hero_img, 0, 0, self.hero_img.width, self.hero_img.height, pyxel.COLOR_PURPLE)
        pyxel.blt(TILE_SIZE*(VIEW_WIDTH+2), 120, self.heroine_img, 0, 0, self.hero_img.width, self.hero_img.height, pyxel.COLOR_PURPLE)
        pyxel.blt(TILE_SIZE*(VIEW_WIDTH+2), 140, self.blackmaze_img, 0, 0, self.hero_img.width, self.hero_img.height, pyxel.COLOR_PURPLE)
        pyxel.blt(TILE_SIZE*(VIEW_WIDTH+2), 160, self.wildhero_img, 0, 0, self.hero_img.width, self.hero_img.height, pyxel.COLOR_PURPLE)