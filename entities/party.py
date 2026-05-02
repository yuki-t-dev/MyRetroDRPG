import pyxel


class Party:
    def __init__(self):
        self.members = []

    def add(self, character):
        self.members.append(character)

    def alive_members(self):
        return [c for c in self.members if c.is_alive()]

    def is_all_dead(self):
        return all(not c.is_alive() for c in self.members)