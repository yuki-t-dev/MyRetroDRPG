import pyxel

from scenes import TitleScene, PlayScene
from constants import (
        GAME_WIDTH,
        GAME_HEIGHT,
        GAME_TITLE,
        )


class Game:
    def __init__(self):
        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=GAME_TITLE)

        self.player = None
        self.hud = None
        self.dungeon = None
        self.scene_name = None

        self.scenes = {
            "title": TitleScene(self),
            "play": PlayScene(self),
        }
        self.change_scene("title")

        pyxel.run(self.update, self.draw)

    def change_scene(self, scene_name):
        self.scene_name = scene_name
        self.scenes[self.scene_name].start()

    def draw_dungeon(self):
        if self.dungeon is not None:
            self.dungeon.draw()

    def draw_player(self):
        if self.player is not None:
            self.player.draw()
    
    def draw_hud(self):
        if self.hud is not None:
            self.hud.draw_floor()
            self.hud.draw_allys()

    def update_dungeon(self):
        if self.dungeon is not None:
            self.dungeon.update()
    
    def update_player(self):
        if self.player is not None:
            self.player.update()

    def update(self):
        self.scenes[self.scene_name].update()

    def draw(self):
        self.scenes[self.scene_name].draw()
