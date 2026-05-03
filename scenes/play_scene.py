import pyxel
import random

from entities import Player
from dungeon import Dungeon
from hud import ViewStatus

from sound import PlayBGM


class PlayScene:
    def __init__(self, game):
        self.game = game
        self.play_bgm = PlayBGM()
        self.initialized = False
        self.steps = 0
        self.next_encounter = random.randint(5, 15)

    def start(self):
        if self.initialized:
            self.play_bgm.play()
            return

        game = self.game
        game.dungeon = Dungeon(game, 64, 64, game.current_floor)
        player_x, player_y = game.dungeon.get_random_floor()
        game.player = Player(game, player_x, player_y)
        game.hud = ViewStatus(game)
        game.dungeon.spawn_goal()
        self.play_bgm.play()

        self.initialized = True

    def update(self):
        self.game.update_dungeon()
        self.game.update_player()
        moved = self.game.player.update()
        if moved:
            self.check_encounter()

    def draw(self):
        pyxel.cls(0)
        self.game.draw_dungeon()
        self.game.draw_player()
        self.game.draw_hud()

    def check_encounter(self):
        self.steps += 1

        if self.steps >= self.next_encounter:
            self.steps = 0
            self.next_encounter = random.randint(5, 15)
            self.game.change_scene("battle")
