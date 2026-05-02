import pyxel

class TitleBGM:
    MELODY = ("t120 l8 o4 v7"
            "c e g >c <g e d c"
            "e g a >c <a g e d"
            "f a >c <a f e d c"
            "g b >d <b g f e d"

            "c e g >c <g e d c"
            "e g a >c <a g e d"
            "f a >c <a f e d c"
            "g >c d e d c <b a g"
    )
    HARMONY = ("t120 l8 o3 v5"
            "c g c g c g c g"
            "a e a e a e a e"
            "f c f c f c f c"
            "g d g d g d g d"

            "c g c g c g c g"
            "a e a e a e a e"
            "f c f c f c f c"
            "g g g g c c c c"
    )
    BASE = ("t120 l4 o2 v6"
            "c c a a f f g g"
            "c c a a f f g g"
            "c c a a f f g g"
            "g g c c"
    )

    def __init__(self):
            self.melody = pyxel.Sound()
            self.melody.mml(self.MELODY)

            self.harmony = pyxel.Sound()
            self.harmony.mml(self.HARMONY)

            self.base = pyxel.Sound()
            self.base.mml(self.BASE)
    def play(self):
        pyxel.play(0, self.melody, loop=True)
        pyxel.play(1, self.harmony, loop=True)
        pyxel.play(2, self.base, loop=True)

class PlayBGM:
    MELODY = ("t90 l8 o4 v7"
            "a g# a e d c# d e"
            "f e d c# d a g# a"
            "a g# a e d c# d e"
            "f e d c# d e f g"

            "a >c a g f e d c"
            "d f d c a g f e"
            "a g# a e d c# d e"
            "a1"
    )
    HARMONY = ("t90 l8 o3 v5"
            "a e a e a e a e"
            "d a d a d a d a"
            "f c f c f c f c"
            "e b e b e b e b"

            "a e a e a e a e"
            "d a d a d a d a"
            "f c f c f c f c"
            "e e e e a a a a"
    )
    BASE = ("t90 l4 o2 v6"
            "a a d d f f e e"
            "a a d d f f e e"
            "a a d d f f e e"
            "e e a a"
    )

    def __init__(self):
        self.melody = pyxel.Sound()
        self.melody.mml(self.MELODY)

        self.harmony = pyxel.Sound()
        self.harmony.mml(self.HARMONY)

        self.base = pyxel.Sound()
        self.base.mml(self.BASE)

    def play(self):
        pyxel.play(0, self.melody, loop=True)
        pyxel.play(1, self.harmony, loop=True)
        pyxel.play(2, self.base, loop=True)

class BattleBGM:
    MELODY = ("t180 l8 o4 v12"
            "e e f g a g f e"
            "d d e f g f e d"
            "c c d e f e d c"
            "b- b- c d e d c b-"
            "o4 f f g a b- a g f"
            "e e f g a g f e"
            "d d e f g f e d"
            "c c d e f e d c"
    )
    HARMONY = ("t180 l8 o3 v5"
            "c g c g d a d a"
            "e b e b f c f c"
            "d a d a e b e b"
            "f c f c g d g d"
    )
    BASE = ("t180 l4 o2 v7"
            "c c g g a a e e"
            "f f c c d d g g"
            "d d a a b b f f"
            "g g d d e e a a"
    )
    DRUMS = ("t180 l16 o1 v10"
            "c r c r c r c r"
            "c c r c c r c r"
    )

    def __init__(self):
        self.melody = pyxel.Sound()
        self.melody.mml(self.MELODY)

        self.harmony = pyxel.Sound()
        self.harmony.mml(self.HARMONY)

        self.base = pyxel.Sound()
        self.base.mml(self.BASE)

        self.drums = pyxel.Sound()
        self.drums.mml(self.DRUMS)

    def play(self):
        pyxel.play(0, self.melody, loop=True)
        pyxel.play(1, self.harmony, loop=True)
        pyxel.play(2, self.base, loop=True)
        pyxel.play(3, self.drums, loop=True)