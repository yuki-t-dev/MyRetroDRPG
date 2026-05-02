import pyxel


class Character:
    def __init__(self, name, hp, mp, atk, defense, file_path):
        self.name = name
        self.max_hp = hp
        self.max_mp = mp
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.file_path = file_path
        self.img = pyxel.Image(16, 16)
        self.img.load(0, 0, f"assets/{self.file_path}")

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        print(self.hp, dmg)
        self.hp = max(0, self.hp - dmg)
