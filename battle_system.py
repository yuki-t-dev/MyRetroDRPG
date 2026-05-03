import pyxel
import random

from constants import TILE_SIZE
from utility import draw_text, decide_color_from_hp

from entities import Enemy

class BattleSystem:
    def __init__(self, game):
        self.game = game
        self.state = "select_actor"
        self.selected_actor = 0
        self.command_idx = 0

        self.commands = ["たたかう", "まほう", "アイテム", "にげる"]
        self.selected_commands = [None] * len(self.game.party.members)

        self.flash_timer = 0
        self.flash_color = pyxel.COLOR_WHITE

        self.enemies = [
            Enemy("スライム", 10, "slime_tachie.png"),
            Enemy("ゴブリン", 20, "goburin_tachie.png"),
        ]

        self.message = "！闘開始始！"

    def draw_battle(self):
        pyxel.cls(0)

        self.draw_allys()
        self.draw_enemies()

        if self.state == "select_command":
            draw_text(200,20,"コマンド？\nA：決定 B：キャンセル", pyxel.COLOR_WHITE, style="shadow")
            self.draw_commands()

        if self.state == "ready":
            draw_text(200,20,"行動開始？\nA：決定 B：キャンセル", pyxel.COLOR_WHITE, style="shadow")

        if self.state in ["action", "win", "select_actor"]:
            draw_text(200,20,self.message, pyxel.COLOR_WHITE, style="shadow")

        if self.flash_timer > 0:
            if self.flash_timer %2 == 0:
                pyxel.rect(0,0,pyxel.width,pyxel.height, self.flash_color)
            self.flash_timer -= 1

    def show_status(self, x, y, member, index):
        pyxel.blt(x, y, member.img, 0, 0, member.img.width, member.img.height, pyxel.COLOR_PURPLE)
        draw_text(x+20, y-2, f":{member.name}", decide_color_from_hp(member), style="shadow")
        draw_text(x+20, y+10, f"HP:{member.hp}/{member.max_hp}", decide_color_from_hp(member), style="shadow")
        draw_text(x+20, y+20, f"MP:{member.mp}/{member.max_mp}", decide_color_from_hp(member), style="shadow")

        cmd = self.selected_commands[index]
        if cmd is None:
            cmd_name = "..."
        else:
            cmd_name = self.commands[cmd["cmd"]]
        draw_text(x+100,y-2,cmd_name, pyxel.COLOR_YELLOW, style="shadow")

    def draw_allys(self):
        for i, member in enumerate(self.game.party.members):
            x = 10 
            y = 10+i*45
            self.show_status(x, y, member, i)

            if i == self.selected_actor:
                pyxel.rectb(x-3, y-3, 85, 35, decide_color_from_hp(member))
                pyxel.blt(140, 160, member.img2, 0, 0, -member.img2.width, member.img2.height, pyxel.COLOR_GREEN)

    def update_battle(self):
        if self.state == "select_actor":
            self.update_select_actor()
        elif self.state == "select_command":
            self.update_select_command()
        elif self.state == "ready":
            self.update_ready()
        elif self.state == "action":
            self.update_action()
        elif self.state == "select_target":
            self.update_select_target()
        elif self.state == "win":
            self.update_win()

    def update_select_actor(self):
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.selected_actor = (self.selected_actor + 1) % len(self.game.party.members)
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.selected_actor = (self.selected_actor - 1) % len(self.game.party.members)

        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.state = "select_command"
            self.command_idx = 0

    def update_select_command(self):
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.command_idx = (self.command_idx + 1) % len(self.commands)
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.command_idx = (self.command_idx - 1) % len(self.commands)

        if pyxel.btnp(pyxel.KEY_B) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.state = "select_actor"
        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.execute_command()
    
    def execute_command(self):
        cmd = self.command_idx

        if cmd == 0:
            self.state = "select_target"
            self.target_idx = 0
            return

        self.selected_commands[self.selected_actor] = {
            "cmd": cmd,
            "target": None
        }

        self.selected_actor += 1

        if all(cmd is not None for cmd in self.selected_commands):
            self.state = "ready"
        else:
            self.state = "select_actor"

    def draw_commands(self):
        if self.state != "select_command":
            return
        x=100
        y=150

        for i, cmd in enumerate(self.commands):
            color = pyxel.COLOR_WHITE
            if i == self.command_idx:
                color = pyxel.COLOR_YELLOW
            draw_text(x, y+i*20, cmd, color, style="shadow")

    def draw_enemies(self):
        for i, enemy in enumerate(self.enemies):
            x=200
            y=60+i*30
            draw_text(x, y, f"{enemy.name} HP:{enemy.hp}", pyxel.COLOR_RED, style="shadow")

            if self.state == "select_target" and i == self.target_idx:
                pyxel.rectb(x-5, y-5, 100, 20, pyxel.COLOR_YELLOW)
                pyxel.blt(250,170,enemy.img,0,0,enemy.img.width,enemy.img.height,pyxel.COLOR_GREEN)

    def update_action(self):
        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            if self.action_idx >= len(self.action_queue):
                self.message = f"次のターン！"
                self.end_turn()
                return
            action = self.action_queue[self.action_idx]
            self.execute_action(action)
            self.action_idx += 1

    def execute_action(self, action):
        actor = action["actor"]

        if not actor.is_alive():
            return

        if action["type"] == "player":
            cmd_data = action["command"]
            cmd = cmd_data["cmd"]

            if cmd == 0:
                target_idx = cmd_data["target"]
                if target_idx is None:
                    return
                target = self.enemies[target_idx]
                damage = random.randint(5, 10)
                target.take_damage(damage)
                se0 = pyxel.Sound()
                se0.mml("T200 O4 L16 V15 E G >C <B A G")
                pyxel.play(3, se0)

                self.flash_timer = 4
                self.flash_color = pyxel.COLOR_WHITE

                self.message = f"{actor.name}の攻撃！\n{target.name}に{damage}のダメージ！"
            elif cmd == 1:
                damage = random.randint(10, 20)
                actor.mp -= 5
                target = random.choice(self.enemies)
                target.take_damage(damage)
                se0 = pyxel.Sound()
                se0.mml("T120 O4 L8 V15 C E G >C <G E C")
                pyxel.play(3, se0)

                self.flash_timer = 6
                self.flash_color = pyxel.COLOR_CYAN

                self.message = f"{actor.name}の魔法！\n敵に{damage}のダメージ！"
            elif cmd == 2:
                self.message = f"{actor.name}はアイテムを使った！"
            elif cmd == 3:
                self.message = f"{actor.name}は逃げ出した！"

        elif action["type"] == "enemy":
            target = random.choice(self.game.party.members)
            damage = random.randint(3, 8)
            target.take_damage(damage)
            se0 = pyxel.Sound()
            se0.mml("T200 O4 L16 V15 E G >C <B A G")
            pyxel.play(3, se0)
            self.flash_timer = 4
            self.flash_color = pyxel.COLOR_WHITE
            self.message = f"{actor.name}の攻撃！\n{target.name}に{damage}のダメージ！"

        alive_enemies = [e for e in self.enemies if e.is_alive()]

        if len(alive_enemies) == 0:
            self.message = f"戦闘に勝利した"
            self.state = "win"
            return

    def update_select_target(self):

        self.enemies = [e for e in self.enemies if e.is_alive()]

        if len(self.enemies) == 0:
            return

        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.target_idx = (self.target_idx + 1) % len(self.enemies)
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.target_idx = (self.target_idx - 1) % len(self.enemies)

        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.selected_commands[self.selected_actor] = {
                "cmd": 0,
                "target":self.target_idx 
            }
            self.selected_actor += 1

            if all(c is not None for c in self.selected_commands):
                self.state = "ready"
            else:
                self.state = "select_actor"
        if pyxel.btnp(pyxel.KEY_B) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.state = "select_command"

    def update_ready(self):
        if pyxel.btnp(pyxel.KEY_B) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.state = "select_command"
            self.selected_actor = 0
        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.message = "全員の行動が決定！"
            self.build_action_queue()
            self.state = "action"
            return

    def end_turn(self):
        self.enemies = [e for e in self.enemies if e.hp > 0]

        self.selected_commands = [None] * len(self.game.party.members)
        self.selected_actor = 0
        self.state = "select_actor"

    def build_action_queue(self):
        self.action_queue = []

        for i, member in enumerate(self.game.party.members):
            cmd = self.selected_commands[i]
            self.action_queue.append({
                "type": "player",
                "actor": member,
                "command": cmd,
            })

        for enemy in self.enemies:
            self.action_queue.append({
                "type": "enemy",
                "actor": enemy,
                "command": 0
            })

        self.action_idx = 0

    def update_win(self):
        if pyxel.btnp(pyxel.KEY_A) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            self.game.change_scene("play")