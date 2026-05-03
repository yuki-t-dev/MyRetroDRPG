import pyxel

from scenes import TitleScene, PlayScene, BattleScene
from constants import (
        GAME_WIDTH,
        GAME_HEIGHT,
        GAME_TITLE,
        )
from entities import Party, Character

class Game:
    def __init__(self):
        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=GAME_TITLE)

        self.player = None

        self.party = Party()
        self.create_party()

        self.hud = None
        self.dungeon = None
        self.scene_name = None
        self.battle = None
        self.current_floor = 1

        self.scenes = {
            "title": TitleScene(self),
            "play": PlayScene(self),
            "battle": BattleScene(self),
        }
        self.change_scene("title")

        pyxel.run(self.update, self.draw)

    def create_party(self):
        self.party.add(Character("マルス", 100, 30, 20, 10, "player.png"))
        self.party.add(Character("マリア", 80, 40, 15, 12, "heroine.png"))
        self.party.add(Character("ビビ", 120, 20, 25, 8, "blackmaze.png"))
        self.party.add(Character("モーグリ", 90, 50, 18, 15, "wildhero.png"))

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

    def draw_battle(self):
        if self.battle is not None:
            self.battle.draw_battle()
            self.battle.draw_allys()

    def update_dungeon(self):
        if self.dungeon is not None:
            self.dungeon.update()
    
    def update_player(self):
        if self.player is not None:
            self.player.update()

    def update(self):
        self.scenes[self.scene_name].update()

    def draw(self):
        print(self.scene_name)
        self.scenes[self.scene_name].draw()
