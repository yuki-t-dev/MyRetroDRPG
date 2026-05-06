import pyxel

from utility import draw_text


class CharSlectSystem:
    MAX_BATTLE = 4

    def __init__(self, game):
        self.game = game
        self.state = "select_charactor"
        self.selected_actor = 0
        self.selectable_members = self.game.party.members
        #self.selectable_members = self.game.party.members[1:]

    def update_selector(self):
        if self.state == "select_charactor":
            self.update_select_charactor()
        if len(self.game.party.battle_party) == self.MAX_BATTLE:
        #if len(self.game.battle_party) == self.MAX_BATTLE:
            self.game.change_scene("play")

    def draw_selector(self):
        pyxel.cls(0)
        self.draw_all_characters()

    def update_select_charactor(self):
        #members = self.game.party.members[1:]
        #max_i = len(members)
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.selected_actor = (self.selected_actor + 1) % len(self.selectable_members) 
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.selected_actor = (self.selected_actor - 1) % len(self.selectable_members)

        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            selected_member = self.selectable_members[self.selected_actor]
            #if selected_member not in self.game.battle_party and \
            if selected_member not in self.game.party.battle_party and \
            len(self.game.party.battle_party) < self.MAX_BATTLE:
            #len(self.game.battle_party) < self.MAX_BATTLE:
                self.game.party.battle_party.append(selected_member)
                #self.game.battle_party.append(selected_member)

    def draw_all_characters(self):
        pyxel.text(0, 0, "test", 7)

        for i, member in enumerate(self.selectable_members):
            row = i % 4
            col = i // 4
            x = 10 + col * 110
            y = 10 + row * 45
            self.show_status(x, y, member, i)

            if i == self.selected_actor:
                pyxel.rectb(x-3, y-3, 85, 35, 7)
                pyxel.blt(140, 160, member.img2, 0, 0, -member.img2.width, member.img2.height, pyxel.COLOR_GREEN)

    def show_status(self, x, y, member, index):
        pyxel.blt(x, y, member.img, 0, 0, member.img.width, member.img.height, pyxel.COLOR_PURPLE)
        draw_text(x+20, y-2, f":{member.name}", 7, style="shadow")
        draw_text(x+20, y+10, f"HP:{member.hp}/{member.max_hp}", 7, style="shadow")
        draw_text(x+20, y+20, f"MP:{member.mp}/{member.max_mp}", 7, style="shadow")