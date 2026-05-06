import pyxel
import random


class Unit:
    def __init__(self, name, hp, mp, atk, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk = atk
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def attack(self, target, skill=None):
        if not self.hit_check(target):
            return {"result": "miss"}

        if skill is None:
            damage, critical = self.physical_attack(target)

        elif skill.type == "physical":
            damage, critical = self.physical_attack(target, skill)

        elif skill.type == "magical":
            if self.mp < 5:
                damage, critical = 0, False
            else:
                damage, critical = self.magical_attack(target, skill)
        
        return {
            "result": "hit",
            "damage": damage,
            "critical": critical
        }
    
    def physical_attack(self, target, skill=None):
        damage = self.calc_damage(target, skill)

        critical = False
        if self.is_critical():
            damage *=2
            critical = True
        target.take_damage(damage)

        return damage, critical

    def magical_attack(self, target, skill):
        damage = self.calc_damage(target, skill=skill)
        target.take_damage(damage)
        self.mp -= 5
        return damage, False

    def calc_damage(self, target, skill=None):
        if skill is None:
            base = self.atk - target.defense
            damage = int(base * random.uniform(0.8, 1.2))
            return max(0, damage)
        elif skill.type == "magical":
            return skill.power

    def hit_check(self, target):
        return True
    
    def is_critical(self):
        return False
