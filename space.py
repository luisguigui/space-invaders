"""
NEON INVADERS: OVERDRIVE EDITION
Desenvolvido por: [LUIS GUILHERME G.B. E OTAVIO CESAR]
"""

import customtkinter as ctk
import tkinter as tk
import random
import time
import json
import os
from dataclasses import dataclass

# Tenta importar pygame para o sistema de som
try:
    import pygame  # pyright: ignore[reportMissingImports]
    pygame.mixer.init()
    SOUND_ENABLED = True
except ImportError:
    SOUND_ENABLED = False


# ============================================================
#  CONSTANTES E DADOS
# ============================================================

CANVAS_W = 900
CANVAS_H = 800
WINDOW_W = 1200
WINDOW_H = 850

SAVE_FILE = "save_data.json"

DROP_TYPES = {
    "SPEED":  {"color": "#1eff00", "label": "⚡"},
    "SHIELD": {"color": "#00fbff", "label": "🛡️"},
    "MULTI":  {"color": "#ffea00", "label": "🔥"},
}

UPGRADES = [
    {"name": "DANO +20%",      "effect": "damage"},
    {"name": "VELOCIDADE +15%","effect": "speed"},
    {"name": "TIRO RÁPIDO",    "effect": "firerate"},
    {"name": "REPARAR ESCUDO", "effect": "hp"},
]


# ============================================================
#  ESTRUTURAS DE DADOS
# ============================================================

@dataclass
class Skin:
    name:      str
    color:     str
    points:    list
    power:     str
    max_hp:    float = 1.0
    damage:    float = 1.0
    fire_rate: float = 0.25
    speed:     float = 520


SKINS = {
    "Interceptor": Skin(
        name="Interceptor", color="#00D4FF",
        points=[(0, -20), (-15, 15), (15, 15)],
        power="BEAM", fire_rate=0.15, speed=600,
    ),
    "Tanker": Skin(
        name="Tanker", color="#FFD700",
        points=[(-20, -10), (20, -10), (20, 20), (-20, 20)],
        power="SHIELD", max_hp=2.5, speed=400,
    ),
    "V-Stinger": Skin(
        name="V-Stinger", color="#FF0055",
        points=[(0, -25), (-20, 10), (0, 0), (20, 10)],
        power="FAN_SHOT", damage=1.8,
    ),
}


class Player:
    """Representa o estado da nave do jogador."""

    def __init__(self, skin: Skin):
        self.skin      = skin
        self.max_hp    = skin.max_hp
        self.hp        = skin.max_hp
        self.damage    = skin.damage
        self.fire_rate = skin.fire_rate
        self.speed     = skin.speed
        self.special   = skin.power
        self.x         = 450
        self.y         = 650


# ============================================================
#  JOGO PRINCIPAL
# ============================================================

class NeonInvaders(ctk.CTk):
    """Classe principal: gerencia UI, lógica e renderização."""

    # --------------------------------------------------------
    #  INICIALIZAÇÃO
    # --------------------------------------------------------

    def __init__(self):
        super().__init__()
        self.title("NEON INVADERS: OVERDRIVE EDITION")
        self.geometry(f"{WINDOW_W}x{WINDOW_H}")
        self.configure(fg_color="#050505")

        # Persistência
        self.high_score = 0
        self._load_progress()

        # Estado do jogo
        self.selected_skin   = "Interceptor"
        self.player          = None
        self.wave            = 1
        self.score           = 0
        self.running         = False
        self.message         = ""
        self.special_charge  = 0.0
        self.shake_intensity = 0
        self.enemy_direction = 1
        self.boss_active     = False

        # Coleções de objetos
        self.enemies       = []
        self.bullets       = []
        self.enemy_bullets = []
        self.specials      = []
        self.drops         = []
        self.particles     = []
        self.stars         = []
        self.barriers      = []
        self.active_powerups = {"SPEED": 0, "MULTI": 0}

        # Controles
        self.keys = {k: False for k in ["left", "right", "up", "down", "space", "x"]}
        self._last_time = 0.0
        self.last_shot  = 0.0

        self._setup_ui()
        self._init_stars()
        self._bind_keys()

        self.after(100, self._open_skin_menu)

    # --------------------------------------------------------
    #  INTERFACE (UI)
    # --------------------------------------------------------

    def _setup_ui(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=280, fg_color="#080808", corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        ctk.CTkLabel(self.sidebar, text="NEON INVADERS",
                     font=("Impact", 32), text_color="#00D4FF").pack(pady=30)

        self.wave_lbl = ctk.CTkLabel(self.sidebar, text="ONDA: 1",
                                     font=("Consolas", 22, "bold"), text_color="#FF00FF")
        self.wave_lbl.pack()

        self.score_lbl = ctk.CTkLabel(self.sidebar, text="PONTOS: 0",
                                      font=("Consolas", 18))
        self.score_lbl.pack(pady=5)

        self.high_score_lbl = ctk.CTkLabel(self.sidebar,
                                            text=f"RECORD: {self.high_score}",
                                            font=("Consolas", 14), text_color="gray")
        self.high_score_lbl.pack(pady=5)

        ctk.CTkLabel(self.sidebar, text="ESCUDOS").pack(pady=(20, 0))
        self.hp_bar = ctk.CTkProgressBar(self.sidebar,
                                         progress_color="#00FF9C", height=12)
        self.hp_bar.set(1.0)
        self.hp_bar.pack(pady=5, padx=20, fill="x")

        ctk.CTkLabel(self.sidebar, text="ESPECIAL (X)").pack(pady=(10, 0))
        self.special_bar = ctk.CTkProgressBar(self.sidebar,
                                              progress_color="#FFD700", height=12)
        self.special_bar.set(0)
        self.special_bar.pack(pady=5, padx=20, fill="x")

        # Frame do boss (ocultado até aparecer)
        self.boss_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.boss_bar = ctk.CTkProgressBar(self.boss_frame,
                                           progress_color="red", height=15)
        self.boss_bar.pack(pady=20, padx=20, fill="x")

        # Canvas do jogo
        self.canvas = tk.Canvas(self, bg="#000", highlightthickness=0)
        self.canvas.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    # --------------------------------------------------------
    #  MENUS
    # --------------------------------------------------------

    def _open_skin_menu(self):
        self.menu_frame = ctk.CTkFrame(self, fg_color="#050505")
        self.menu_frame.place(relwidth=1, relheight=1)

        ctk.CTkLabel(self.menu_frame, text="ESCOLHA SUA NAVE",
                     font=("Impact", 45), text_color="#00D4FF").pack(pady=40)

        self.skin_preview = tk.Canvas(self.menu_frame, width=200, height=200,
                                      bg="#000", highlightthickness=0)
        self.skin_preview.pack(pady=10)

        self.skin_info = ctk.CTkLabel(self.menu_frame, text="",
                                      font=("Consolas", 18))
        self.skin_info.pack(pady=10)

        btn_frame = ctk.CTkFrame(self.menu_frame, fg_color="transparent")
        btn_frame.pack(pady=20)
        for name in SKINS:
            ctk.CTkButton(btn_frame, text=name, width=120,
                          command=lambda n=name: self._select_skin_ui(n)).pack(side="left", padx=10)

        ctk.CTkButton(self.menu_frame, text="DECOLAR",
                      height=60, width=300, font=("Impact", 24),
                      fg_color="#d35400", command=self._start_game).pack(pady=40)

        self._select_skin_ui(self.selected_skin)

    def _select_skin_ui(self, name: str):
        self.selected_skin = name
        skin = SKINS[name]
        self.skin_info.configure(
            text=f"{skin.name}\nHP: {skin.max_hp} | SPD: {skin.speed}\nPOWER: {skin.power}"
        )
        self.skin_preview.delete("all")
        self.skin_preview.create_polygon(
            [(100 + dx * 2, 100 + dy * 2) for dx, dy in skin.points],
            fill=skin.color, outline="white"
        )

    def _open_upgrade_menu(self):
        self.running = False
        self.upgrade_frame = ctk.CTkFrame(self, fg_color="#050505")
        self.upgrade_frame.place(relwidth=1, relheight=1)

        ctk.CTkLabel(self.upgrade_frame, text="ONDA LIMPA!",
                     font=("Impact", 50), text_color="#00FF9C").pack(pady=30)
        ctk.CTkLabel(self.upgrade_frame, text="ESCOLHA UM UPGRADE",
                     font=("Impact", 25)).pack(pady=10)

        for up in random.sample(UPGRADES, 3):
            ctk.CTkButton(
                self.upgrade_frame, text=up["name"],
                width=300, height=60, font=("Consolas", 18),
                command=lambda e=up["effect"]: self._apply_upgrade(e)
            ).pack(pady=10)

        self._save_progress()

    def _apply_upgrade(self, effect: str):
        if effect == "damage":   self.player.damage *= 1.2
        elif effect == "speed":  self.player.speed  *= 1.15
        elif effect == "firerate":
            self.player.fire_rate = max(0.08, self.player.fire_rate * 0.8)
        elif effect == "hp":
            self.player.max_hp += 0.5
            self.player.hp = self.player.max_hp

        self.upgrade_frame.destroy()
        self.running = True
        self._spawn_logic()
        self._game_loop()

    # --------------------------------------------------------
    #  CONTROLE DO JOGO
    # --------------------------------------------------------

    def _start_game(self):
        if hasattr(self, "menu_frame"):
            self.menu_frame.destroy()
        self.player = Player(SKINS[self.selected_skin])
        self.running = True
        self.wave    = 1
        self.score   = 0
        self.active_powerups = {"SPEED": 0, "MULTI": 0}
        self._create_barriers()
        self._spawn_logic()
        self._last_time = time.perf_counter()
        self._game_loop()

    def _spawn_logic(self):
        self.enemies.clear()
        self.bullets.clear()
        self.enemy_bullets.clear()
        self.drops.clear()
        self.message = ""
        self.enemy_direction = 1

        self.score_lbl.configure(text=f"PONTOS: {self.score}")
        self.wave_lbl.configure(text=f"ONDA: {self.wave}")

        if self.wave % 5 == 0:
            self._spawn_boss()
        else:
            self._spawn_enemies()

    def _spawn_boss(self):
        self.boss_active  = True
        self.boss_max_hp  = 50 + (self.wave * 15)
        self.boss_hp      = self.boss_max_hp
        self.boss_x       = 350
        self.boss_dir     = 1
        self.boss_phase   = 1
        self.boss_bar.set(1.0)
        self.boss_frame.pack(fill="x")

    def _spawn_enemies(self):
        self.boss_active = False
        self.boss_frame.pack_forget()
        rows = min(6, 2 + (self.wave // 3))
        for r in range(rows):
            for c in range(8):
                etype = "SHOOTER" if random.random() < 0.2 else "NORMAL"
                self.enemies.append({"x": 100 + c * 85, "y": 70 + r * 55, "type": etype})

    def _game_over(self):
        self.running = False
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_progress()
        self.canvas.create_text(450, 350, text="GAME OVER",
                                fill="red", font=("Impact", 80))
        self.after(3000, self._open_skin_menu)

    # --------------------------------------------------------
    #  LÓGICA DE ATUALIZAÇÃO
    # --------------------------------------------------------

    def _update_logic(self, dt: float):
        if not self.running or self.message:
            return

        self._update_shake(dt)
        self._update_stars(dt)
        self._update_powerup_timers(dt)
        self._update_player_movement(dt)
        self._update_player_shoot()
        self._update_special()

        if self.boss_active:
            self._update_boss(dt)
        else:
            self._update_enemies(dt)

        self._update_player_bullets(dt)
        self._update_enemy_bullets(dt)
        self._update_particles()
        self._update_drops(dt)
        self._update_specials(dt)
        self._cleanup_barriers()
        self._check_wave_clear()

        self.special_bar.set(self.special_charge)
        self.hp_bar.set(max(0, self.player.hp / self.player.max_hp))

    def _update_shake(self, dt: float):
        if self.shake_intensity > 0:
            self.shake_intensity -= 15 * dt

    def _update_stars(self, dt: float):
        for s in self.stars:
            s["y"] += s["s"] * 50 * dt
            if s["y"] > CANVAS_H:
                s["y"] = 0
                s["x"] = random.randint(0, CANVAS_W)

    def _update_powerup_timers(self, dt: float):
        for k in self.active_powerups:
            if self.active_powerups[k] > 0:
                self.active_powerups[k] -= dt

    def _update_player_movement(self, dt: float):
        spd = self.player.speed * (1.6 if self.active_powerups["SPEED"] > 0 else 1.0)
        if self.keys["left"]  and self.player.x > 40:       self.player.x -= spd * dt
        if self.keys["right"] and self.player.x < CANVAS_W - 90: self.player.x += spd * dt

    def _update_player_shoot(self):
        now = time.perf_counter()
        if self.keys["space"] and now - self.last_shot > self.player.fire_rate:
            self._play_sound("shoot")
            if self.active_powerups["MULTI"] > 0:
                for vx in (-180, 0, 180):
                    self.bullets.append({"x": self.player.x, "y": self.player.y - 20, "vx": vx})
            else:
                self.bullets.append({"x": self.player.x, "y": self.player.y - 20, "vx": 0})
            self.last_shot = now

    def _update_special(self):
        if self.keys["x"] and self.special_charge >= 1.0:
            self._activate_special()

    def _activate_special(self):
        self.special_charge = 0.0
        self._play_sound("special")
        if self.player.special == "BEAM":
            self.specials.append({"type": "BEAM",   "timer": 2.0})
        elif self.player.special == "SHIELD":
            self.specials.append({"type": "SHIELD", "timer": 6.0})
        elif self.player.special == "FAN_SHOT":
            for vx in range(-300, 301, 100):
                self.bullets.append({"x": self.player.x, "y": self.player.y, "vx": vx})

    def _update_boss(self, dt: float):
        hp_ratio = self.boss_hp / self.boss_max_hp
        if   hp_ratio < 0.3: self.boss_phase = 3
        elif hp_ratio < 0.7: self.boss_phase = 2
        else:                self.boss_phase = 1

        self.boss_x += (220 + self.boss_phase * 50) * dt * self.boss_dir
        if self.boss_x > 680 or self.boss_x < 50:
            self.boss_dir *= -1

        fire_chance = 0.05 + self.boss_phase * 0.03
        if random.random() < fire_chance:
            if self.boss_phase == 1: vxs = [0]
            elif self.boss_phase == 2: vxs = [-150, 0, 150]
            else: vxs = [-250, -120, 0, 120, 250]
            for vx in vxs:
                self.enemy_bullets.append({"x": self.boss_x + 75, "y": 120, "vx": vx})

    def _update_enemies(self, dt: float):
        move_down = False
        for e in self.enemies:
            e["x"] += (110 + self.wave * 10) * dt * self.enemy_direction
            if (e["x"] > 820 and self.enemy_direction == 1) or \
               (e["x"] < 30  and self.enemy_direction == -1):
                move_down = True

            fire_chance = 0.015 if e["type"] == "SHOOTER" else 0.004
            if random.random() < fire_chance:
                self.enemy_bullets.append({"x": e["x"] + 20, "y": e["y"] + 30, "vx": 0})

        if move_down:
            self.enemy_direction *= -1
            for e in self.enemies:
                e["y"] += 35

    def _update_player_bullets(self, dt: float):
        for b in self.bullets[:]:
            b["y"] -= 800 * dt
            b["x"] += b.get("vx", 0) * dt

            if b["y"] < 0 or b["x"] < 0 or b["x"] > CANVAS_W:
                self.bullets.remove(b)
                continue

            if self._bullet_hits_barrier(b):
                if b in self.bullets:
                    self.bullets.remove(b)
                continue

            if self.boss_active:
                self._check_bullet_hits_boss(b)
            else:
                self._check_bullet_hits_enemy(b)

    def _bullet_hits_barrier(self, b: dict) -> bool:
        for br in self.barriers:
            if br["x"] < b["x"] < br["x"] + br["w"] and br["y"] < b["y"] < br["y"] + br["h"]:
                br["hp"] -= 1
                return True
        return False

    def _check_bullet_hits_boss(self, b: dict):
        if self.boss_x < b["x"] < self.boss_x + 150 and 50 < b["y"] < 120:
            self.boss_hp -= self.player.damage
            self.boss_bar.set(max(0, self.boss_hp / self.boss_max_hp))
            self._spawn_particles(b["x"], b["y"], "red")
            if b in self.bullets:
                self.bullets.remove(b)
            if self.boss_hp <= 0:
                self.score += 2000
                self.boss_active = False
                self.message = "BOSS DESTRUÍDO!"
                self.after(1500, self._open_upgrade_menu)

    def _check_bullet_hits_enemy(self, b: dict):
        for e in self.enemies[:]:
            if e["x"] < b["x"] < e["x"] + 40 and e["y"] < b["y"] < e["y"] + 35:
                self._play_sound("explosion")
                self._spawn_particles(e["x"] + 20, e["y"] + 15, "#00FF9C")
                if random.random() < 0.15:
                    self.drops.append({
                        "x": e["x"] + 20, "y": e["y"] + 15,
                        "type": random.choice(list(DROP_TYPES.keys()))
                    })
                self.enemies.remove(e)
                self.score += 100
                self.special_charge = min(1.0, self.special_charge + 0.05)
                if b in self.bullets:
                    self.bullets.remove(b)
                break

    def _update_enemy_bullets(self, dt: float):
        shielded = any(s["type"] == "SHIELD" for s in self.specials)
        for eb in self.enemy_bullets[:]:
            eb["y"] += 450 * dt

            if self._enemy_bullet_hits_barrier(eb):
                continue

            if abs(eb["x"] - self.player.x) < 25 and abs(eb["y"] - self.player.y) < 25:
                if not shielded:
                    self.player.hp -= 0.1
                    self.shake_intensity = 10
                    self._play_sound("hit")
                self.enemy_bullets.remove(eb)
                if self.player.hp <= 0:
                    self._game_over()
            elif eb["y"] > CANVAS_H:
                self.enemy_bullets.remove(eb)

    def _enemy_bullet_hits_barrier(self, eb: dict) -> bool:
        for br in self.barriers:
            if br["x"] < eb["x"] < br["x"] + br["w"] and br["y"] < eb["y"] < br["y"] + br["h"]:
                br["hp"] -= 1
                if eb in self.enemy_bullets:
                    self.enemy_bullets.remove(eb)
                return True
        return False

    def _update_particles(self):
        for p in self.particles[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 0.05
            if p["life"] <= 0:
                self.particles.remove(p)

    def _update_drops(self, dt: float):
        for d in self.drops[:]:
            d["y"] += 200 * dt
            if abs(d["x"] - self.player.x) < 35 and abs(d["y"] - self.player.y) < 35:
                self._play_sound("upgrade")
                if   d["type"] == "SPEED":  self.active_powerups["SPEED"] = 7.0
                elif d["type"] == "MULTI":  self.active_powerups["MULTI"] = 6.0
                elif d["type"] == "SHIELD":
                    self.specials.append({"type": "SHIELD", "timer": 5.0})
                self.drops.remove(d)
            elif d["y"] > CANVAS_H:
                self.drops.remove(d)

    def _update_specials(self, dt: float):
        for s in self.specials[:]:
            if s["type"] == "BEAM":
                for e in self.enemies[:]:
                    if abs(e["x"] - self.player.x) < 30:
                        self.enemies.remove(e)
                        self.score += 50
                if self.boss_active and abs(self.boss_x + 75 - self.player.x) < 50:
                    self.boss_hp -= 0.2
            s["timer"] -= dt
            if s["timer"] <= 0:
                self.specials.remove(s)

    def _cleanup_barriers(self):
        self.barriers = [b for b in self.barriers if b["hp"] > 0]

    def _check_wave_clear(self):
        if not self.enemies and not self.boss_active and not self.message:
            self.message = "ONDA LIMPA!"
            self.wave += 1
            self.after(1500, self._open_upgrade_menu)

    # --------------------------------------------------------
    #  RENDERIZAÇÃO
    # --------------------------------------------------------

    def _draw(self):
        self.canvas.delete("all")
        ox = random.uniform(-self.shake_intensity, self.shake_intensity)
        oy = random.uniform(-self.shake_intensity, self.shake_intensity)

        self._draw_stars()
        self._draw_barriers(ox, oy)
        self._draw_particles()
        self._draw_specials(ox, oy)
        self._draw_player(ox, oy)
        self._draw_enemies(ox, oy)
        self._draw_boss(ox, oy)
        self._draw_bullets(ox, oy)
        self._draw_drops(ox, oy)
        self._draw_messages()

    def _draw_stars(self):
        for s in self.stars:
            self.canvas.create_oval(s["x"], s["y"],
                                    s["x"] + 2, s["y"] + 2, fill="#333")

    def _draw_barriers(self, ox: float, oy: float):
        for br in self.barriers:
            self.canvas.create_rectangle(
                br["x"] + ox, br["y"] + oy,
                br["x"] + br["w"] + ox, br["y"] + br["h"] + oy,
                outline="#00ff9c", width=2
            )

    def _draw_particles(self):
        for p in self.particles:
            self.canvas.create_rectangle(
                p["x"], p["y"], p["x"] + 3, p["y"] + 3,
                fill=p["color"], outline=""
            )

    def _draw_specials(self, ox: float, oy: float):
        for s in self.specials:
            if s["type"] == "SHIELD":
                self.canvas.create_oval(
                    self.player.x - 50 + ox, self.player.y - 50 + oy,
                    self.player.x + 50 + ox, self.player.y + 50 + oy,
                    outline="#00fbff", width=2
                )
            if s["type"] == "BEAM":
                self.canvas.create_line(
                    self.player.x + ox, self.player.y + oy,
                    self.player.x + ox, 0,
                    fill="#00D4FF", width=10
                )

    def _draw_player(self, ox: float, oy: float):
        pts = [(self.player.x + dx + ox, self.player.y + dy + oy)
               for dx, dy in self.player.skin.points]
        self.canvas.create_polygon(pts, fill=self.player.skin.color, outline="white")

    def _draw_enemies(self, ox: float, oy: float):
        for e in self.enemies:
            color = "#FF00FF" if e["type"] == "SHOOTER" else "#00FF9C"
            self.canvas.create_rectangle(
                e["x"] + ox,      e["y"] + oy,
                e["x"] + 40 + ox, e["y"] + 30 + oy,
                outline=color, width=2
            )

    def _draw_boss(self, ox: float, oy: float):
        if self.boss_active:
            self.canvas.create_rectangle(
                self.boss_x + ox,       60 + oy,
                self.boss_x + 150 + ox, 110 + oy,
                outline="red", width=3
            )

    def _draw_bullets(self, ox: float, oy: float):
        for b in self.bullets:
            self.canvas.create_line(
                b["x"] + ox, b["y"] + oy,
                b["x"] + ox, b["y"] + 10 + oy,
                fill="white", width=2
            )
        for eb in self.enemy_bullets:
            self.canvas.create_oval(
                eb["x"] - 4 + ox, eb["y"] - 4 + oy,
                eb["x"] + 4 + ox, eb["y"] + 4 + oy,
                fill="red"
            )

    def _draw_drops(self, ox: float, oy: float):
        for d in self.drops:
            cfg = DROP_TYPES[d["type"]]
            self.canvas.create_text(
                d["x"] + ox, d["y"] + oy,
                text=cfg["label"], fill=cfg["color"],
                font=("Arial", 14, "bold")
            )

    def _draw_messages(self):
        if self.message:
            self.canvas.create_text(
                450, 350, text=self.message,
                fill="#FF00FF", font=("Impact", 50)
            )

    # --------------------------------------------------------
    #  LOOP PRINCIPAL
    # --------------------------------------------------------

    def _game_loop(self):
        if not self.running:
            return
        now = time.perf_counter()
        dt  = now - self._last_time
        self._last_time = now
        self._update_logic(dt)
        self._draw()
        self.after(16, self._game_loop)

    # --------------------------------------------------------
    #  UTILITÁRIOS
    # --------------------------------------------------------

    def _init_stars(self):
        self.stars = [
            {"x": random.randint(0, CANVAS_W),
             "y": random.randint(0, CANVAS_H),
             "s": random.uniform(0.5, 2.5)}
            for _ in range(100)
        ]

    def _create_barriers(self):
        self.barriers = [
            {"x": 150 + i * 200, "y": 550, "hp": 10, "w": 80, "h": 15}
            for i in range(4)
        ]

    def _spawn_particles(self, x: float, y: float, color: str):
        for _ in range(5):
            self.particles.append({
                "x": x, "y": y,
                "vx": random.uniform(-3, 3),
                "vy": random.uniform(-3, 3),
                "life": 1.0, "color": color,
            })

    def _play_sound(self, name: str):
        if SOUND_ENABLED:
            try:
                pygame.mixer.Sound(f"sounds/{name}.wav").play()
            except Exception:
                pass

    def _save_progress(self):
        with open(SAVE_FILE, "w") as f:
            json.dump({"high_score": self.high_score}, f)

    def _load_progress(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                self.high_score = json.load(f).get("high_score", 0)

    def _bind_keys(self):
        self.bind("<KeyPress>",   lambda e: self._handle_key(e, True))
        self.bind("<KeyRelease>", lambda e: self._handle_key(e, False))

    def _handle_key(self, event, state: bool):
        k = event.keysym.lower()
        if k in self.keys:
            self.keys[k] = state


# ============================================================
#  ENTRADA
# ============================================================

if __name__ == "__main__":
    app = NeonInvaders()
    app.mainloop()