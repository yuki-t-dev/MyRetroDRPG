import pyxel


class Enemy:
    def __init__(self, name, hp, file_path):
        self.name = name
        self.hp = hp
        self.file_path = file_path
        self.img = pyxel.Image(100, 100)
        self.img.load(0, 0, f"assets/{self.file_path}")
    
    def is_alive(self):
        return self.hp>0

    def take_damage(self, damage):
        self.hp -= damage
        self.hp = max(0, self.hp)