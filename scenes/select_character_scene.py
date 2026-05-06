import pyxel

from charactor_select_system import CharSlectSystem

from entities import Character


class SelectCharScene:
    def __init__(self, game):
        self.game = game
    def start(self):
        game = self.game
        game.party.battle_party = []
        game.party.battle_party.append(Character("マルス", 120, 30, 20, 10, "player.png"))
        game.select = CharSlectSystem(game)

    def update(self):
        self.game.select.update_selector()
    def draw(self):
        self.game.select.draw_selector()