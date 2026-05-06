import pyxel

from entities.unit import Unit


class Enemy(Unit):
    def __init__(self, name, hp, mp, atk, defense, file_path):
        super().__init__(name, hp, mp, atk, defense)

        self.file_path = file_path
        self.img = pyxel.Image(100, 100)
        self.img.load(0, 0, f"assets/{self.file_path}")
