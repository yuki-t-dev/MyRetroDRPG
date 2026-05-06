import pyxel

from scenes import TitleScene, PlayScene, BattleScene, OpeningRollScene, BeforeBattle, AfterBattle, SelectCharScene
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
        self.boss_floor = 3
        self.select = None

        self.scenes = {
            "title": TitleScene(self),
            "opening": OpeningRollScene(self),
            "select": SelectCharScene(self),
            "play": PlayScene(self),
            "battle": BattleScene(self),
            "before": BeforeBattle(self),
            "after": AfterBattle(self)
        }
        self.change_scene("title")
        #self.change_scene("select")
        #self.change_scene("battle")

        pyxel.run(self.update, self.draw)

    def create_party(self):
        self.party.add(Character("マリア", 100, 40, 15, 12, "heroine.png"))
        self.party.add(Character("ビビ", 100, 70, 10, 15, "blackmaze.png"))
        self.party.add(Character("モーグリ", 100, 50, 20, 15, "wildhero.png"))
        self.party.add(Character("博士", 90, 100, 10, 15, "doctor.png"))
        self.party.add(Character("ナナキ", 130, 20, 20, 20, "wilddog.png"))
        self.party.add(Character("配管工", 150, 0, 25, 20, "plumber.png"))
        self.party.add(Character("ワニ", 140, 0, 20, 25, "wani.png"))
        self.party.battle_party.append(Character("マルス", 200, 15, 20, 20, "player.png"))

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
