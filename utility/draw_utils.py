import pyxel


_fonts = {}

def get_font(name="normal"):
    if name not in _fonts:
        _fonts[name] = pyxel.Font("./assets/umplus_j10r.bdf")
    return _fonts[name]

def draw_text(x, y, text, col=7, style="normal", font="normal", **kwargs):
    f = get_font()

    if style == "shadow":
        pyxel.text(x+1, y, text, kwargs.get("shadow_col", pyxel.COLOR_DARK_BLUE), f)

    elif style == "outline":
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            pyxel.text(x+dx, y+dy, text, kwargs.get("outline_col", 0), f)

    pyxel.text(x, y, text, col, f)

def decide_color_from_hp(member):
    if member.hp <= 0:
        return pyxel.COLOR_RED
    elif member.hp <= member.max_hp * 0.3:
        return pyxel.COLOR_YELLOW
    else:
        return pyxel.COLOR_WHITE
