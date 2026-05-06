import pyxel

from utility import draw_text
from sound import OpeningBGM

class OpeningRollScene:
    def __init__(self, game):
        self.game = game
        self.open_roll_img = pyxel.Image(324, 240)
        self.open_roll_img.load(0, 0, "assets/openroll.png")
        self.lines = [
            "闇に覆われた時代――",
            "人々は、地の底に広がる“古の迷宮”を恐れていた。",
            "",
            "かつて栄えた王国は、",
            "その深淵より現れた災厄によって滅びたという。",
            "",
            "そして今、再び――",
            "迷宮は目を覚ました。",
            "ひとりの若き勇者が立ち上がる。",
            "志を同じくする仲間たちと共に。",
            "",
            "剣を握る者、魔を操る者、",
            "それぞれの想いを胸に――",
            "",
            "彼らは、迷宮の奥へと足を踏み入れる。",
            "",
            "1階――静寂。",
            "2階――ざわめき。",
            "",
            "そして、3階。",
            "",
            "そこには、",
            "“何か”が待っている。",
            "",
            "それは救いか。",
            "それとも――",
            "",
            "絶望か。",
            "",
            "運命は、まだ誰も知らない。",
        ]

        self.line_index = 0
        self.char_index = 0
        self.frame_wait = 2

        self.opening_bgm = OpeningBGM()

    def update(self):
        if pyxel.frame_count % self.frame_wait == 0:
            if self.char_index < len(self.lines[self.line_index]):
                self.char_index += 1

        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            if self.char_index < len(self.lines[self.line_index]):
                self.char_index = len(self.lines[self.line_index])
            else:
                if self.line_index == len(self.lines) - 1:
                    self.game.change_scene("play")
                else:
                    self.line_index += 1
                    self.char_index = 0

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, self.open_roll_img, 0, 0, self.open_roll_img.width, self.open_roll_img.height)

        text = self.lines[self.line_index][:self.char_index]

        draw_text(10, 60, text, 7,style="shadow")

        if self.char_index == len(self.lines[self.line_index]):
            draw_text(200, 120, "▼", 7)
    def start(self):
        self.line_index = 0
        self.char_index = 0
        self.opening_bgm.play()