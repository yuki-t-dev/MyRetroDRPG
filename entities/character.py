import pyxel

from entities.unit import Unit


class Character(Unit):
    def __init__(self, name, hp, mp, atk, defense, file_path):
        super().__init__(name, hp, mp)

        #self.max_mp = mp
        #self.mp = mp
        self.atk = atk
        self.defense = defense
        self.file_path = file_path
        self.img = pyxel.Image(16, 16)
        self.img2 = pyxel.Image(80, 80)
        self.img.load(0, 0, f"assets/{self.file_path}")
        self.img2.load(0, 0, f"assets/{self.file_path[:-4]}_tachie.png")

class Skill:
    def __init__(self, name, power, skill_type):
        self.name = name
        self.power = power
        self.type = skill_type