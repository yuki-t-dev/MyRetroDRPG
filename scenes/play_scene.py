import pyxel

from entities import Player
from dungeon import Dungeon
from hud import ViewStatus


class PlayScene:
    def __init__(self, game):
        self.game = game

    def start(self):
        game = self.game
        game.dungeon = Dungeon(game, 64, 64)
        player_x, player_y = game.dungeon.get_random_floor()
        game.player = Player(game, player_x, player_y)
        game.hud = ViewStatus(game)
        game.dungeon.spawn_goal()
        game.dungeon.update_fov(player_x, player_y)



    def update(self):
        self.game.update_dungeon()
        self.game.update_player()

    def draw(self):
        pyxel.cls(0)
        self.game.draw_dungeon()
        self.game.draw_player()
        self.game.draw_hud()