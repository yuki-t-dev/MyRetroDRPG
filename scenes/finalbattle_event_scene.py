import pyxel

from utility import draw_text

from sound import EndingBGM

class BeforeBattle:
    def __init__(self, game):
        self.game = game
        self.before_battle_img = pyxel.Image(324, 240)
        self.before_battle_img.load(0, 0, "assets/before_dragon_battle.png")

        self.lines = [
            "「……来たか。愚かな人間どもよ。」",
            "",
            "「この深淵に足を踏み入れた時点で、",
            "貴様らの運命は決していたのだ。」",
            "",
            "「かつてこの地を滅ぼした“災厄”――",
            "それが何か、理解しているか？」",
            "",
            "「……そうだ。俺だ。」",
            "",
            "「王も、兵も、すべて焼き尽くした。",
            "叫びも、祈りも、何一つ届きはしなかった。」",
            "",
            "「それでもなお、挑むか？」",
            "",
            "「……いいだろう。」",
            "",
            "「その小さき希望ごと、",
            "灰にしてやる。」",
            "",
            "「来い――勇者よ。」",
        ]
        self.line_index = 0
        self.char_index = 0
        self.frame_wait = 2

    def start(self):
        self.line_index = 0
        self.char_index = 0

    def update(self):
        if pyxel.frame_count % self.frame_wait == 0:
            if self.char_index < len(self.lines[self.line_index]):
                self.char_index += 1

        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            if self.char_index < len(self.lines[self.line_index]):
                self.char_index = len(self.lines[self.line_index])
            else:
                if self.line_index == len(self.lines) - 1:
                    self.game.change_scene("battle")
                else:
                    self.line_index += 1
                    self.char_index = 0
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, self.before_battle_img, 0, 0, self.before_battle_img.width, self.before_battle_img.height)

        text = self.lines[self.line_index][:self.char_index]

        draw_text(10, 60, text, 7,style="shadow")

        if self.char_index == len(self.lines[self.line_index]):
            draw_text(200, 120, "▼", 7)

class AfterBattle:
    def __init__(self, game):
        self.game = game
        self.ending_img = pyxel.Image(324, 240)
        self.ending_img.load(0, 0, "assets/ending.png")

        self.ending_bgm = EndingBGM()

        self.lines = [
            "――激闘の果てに。",
            "深淵を支配していた災厄は、",
            "ついにその息の根を止められた。",
            "長きにわたり閉ざされていた迷宮は、",
            "静寂を取り戻す。",
            "それは、",
            "恐怖の終わりであり――",
            "新たな始まりでもあった。",
            "地上では、",
            "人々が再び空を見上げるようになった。",
            "怯えではなく、",
            "希望を胸に。",
            "名もなき勇者と、その仲間たち。",
            "彼らの名は、",
            "やがて語り継がれるだろう。",
            "闇を払いし者たちとして。",
            "だが――",
            "迷宮の奥底に残されたものを、",
            "まだ誰も知らない。",
            "それは、",
            "完全な終焉か。",
            "それとも――",
            "新たなる災いの兆しか。",
            "物語は終わらない。",
            "そしてまた、",
            "新たな冒険が始まる。",
            "           ――END――",
        ]
        self.line_index = 0
        self.char_index = 0
        self.frame_wait = 2

    def start(self):
        self.line_index = 0
        self.char_index = 0
        self.ending_bgm.play()

    def update(self):
        if pyxel.frame_count % self.frame_wait == 0:
            if self.char_index < len(self.lines[self.line_index]):
                self.char_index += 1

        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            if self.char_index < len(self.lines[self.line_index]):
                self.char_index = len(self.lines[self.line_index])
            else:
                if self.line_index == len(self.lines) - 1:
                    self.game.change_scene("title")
                else:
                    self.line_index += 1
                    self.char_index = 0
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, self.ending_img, 0, 0, self.ending_img.width, self.ending_img.height)

        text = self.lines[self.line_index][:self.char_index]

        draw_text(10, 60, text, 7,style="shadow")

        if self.char_index == len(self.lines[self.line_index]):
            draw_text(200, 120, "▼", 7)
