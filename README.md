# 🛸 NEON INVADERS: OVERDRIVE EDITION

> Um arcade futurista e frenético em Python, onde você pilota naves únicas com poderes especiais para enfrentar hordas neon e chefões épicos. Escolha sua nave, domine upgrades estratégicos e sobreviva às ondas infinitas com estilo retro-futurista vibrante.

[![Python](https://img.shields.io/badge/python-3.8+-3776ab.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Latest-blue.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Pygame](https://img.shields.io/badge/Pygame-Mixer-Optional-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)]()

<div align="center">

**[🚀 Instalação](#-instalação-e-execução) • [📖 Documentação](#-arquitetura-e-estrutura) • [🎮 Como Jogar](#-como-jogar) • [🛠️ Tecnologias](#️-tecnologias-utilizadas) • [⚙️ Configuração](#️-configuração-avançada)**

</div>

---

## 🌟 Visão Geral

**NEON INVADERS: OVERDRIVE EDITION** é um jogo de tiros arcade (Shoot 'em Up) de alto desempenho desenvolvido em Python. Combina **mecânicas clássicas de arcade** com **sistemas modernos de progressão**, oferecendo uma experiência envolvente com desafios escaláveis e recompensas satisfatórias.

O jogo foi desenvolvido em **colaboração** entre **Luis Guilherme G.B.** e **Otavio Cesar**, demonstrando trabalho em equipe e desenvolvimento modular.

### ✨ Destaques Principais

- 🚀 **3 Naves Únicas**: Cada uma com atributos distintos (HP, velocidade, dano, poder especial)
- 💥 **Mecânicas Especiais**: BEAM (laser), SHIELD (escudo) e FAN_SHOT (chuva de balas)
- 🌊 **Sistema de Ondas**: Inimigos progressivamente mais fortes + Bosses a cada 5 ondas
- ⚡ **PowerUps Dinâmicos**: SPEED, MULTI-TIRO, e ESCUDO caem dos inimigos
- 🎖️ **Upgrades Estratégicos**: Escolha entre dano, velocidade, taxa de disparo ou reparo
- 🎨 **Estética Neon**: Paleta de cores cyberpunk com efeitos de partículas e screen shake
- 💾 **Persistência**: High score salvo automaticamente
- 🎵 **Áudio Opcional**: Suporte a som via pygame.mixer (opcional)

---

## 🎮 Como Jogar

### 🎯 Objetivo
Sobreviva o máximo de ondas possível, destruindo inimigos e chefes para acumular pontos e desbloquear upgrades que o tornem mais poderoso.

### 📋 Controles

| Tecla | Ação |
|-------|------|
| ⬅️ **LEFT** | Mover nave para esquerda |
| ➡️ **RIGHT** | Mover nave para direita |
| 🔫 **SPACE** | Disparar (continuo) |
| ⚡ **X** | Ativar Poder Especial (quando barra estiver cheia) |

### 🛸 Escolha de Naves

#### 1️⃣ **Interceptor** ⚡ (Recomendado para iniciantes)

```
        ◁
       ◀▶
      ◀ ▶
```

| Atributo | Valor |
|----------|-------|
| **HP** | 1.0 (médio) |
| **Velocidade** | 600 (mais rápida) |
| **Dano** | 1.0 (padrão) |
| **Taxa de Disparo** | 0.15s (rápida) |
| **Poder Especial** | 🔷 **BEAM** |

**Estratégia**: Use a velocidade para esquivar, mantenha distância dos inimigos. O BEAM é perfeito para limpar hordas.

**Poder BEAM**: Laser contínuo que destrói todos os inimigos na sua coluna por 2 segundos.

---

#### 2️⃣ **Tanker** 🛡️ (Recomendado para defensiva)

```
   ┌──────┐
   │░░░░░░│
   └──────┘
```

| Atributo | Valor |
|----------|-------|
| **HP** | 2.5 (muito alto) |
| **Velocidade** | 400 (mais lenta) |
| **Dano** | 1.0 (padrão) |
| **Taxa de Disparo** | 0.25s (normal) |
| **Poder Especial** | 🛡️ **SHIELD** |

**Estratégia**: Resista a mais dano e ganhe tempo. Use o SHIELD defensivamente.

**Poder SHIELD**: Cria um escudo protetor ao redor da nave por 6 segundos, bloqueando todos os disparos inimigos.

---

#### 3️⃣ **V-Stinger** 🔥 (Recomendado para ataque)

```
      △
     ◀ ▶
       V
```

| Atributo | Valor |
|----------|-------|
| **HP** | 1.0 (médio) |
| **Velocidade** | 520 (rápida) |
| **Dano** | 1.8 (muito alto) |
| **Taxa de Disparo** | 0.25s (normal) |
| **Poder Especial** | 🔥 **FAN_SHOT** |

**Estratégia**: Atire primeiro, pense depois. O alto dano compensa a falta de velocidade.

**Poder FAN_SHOT**: Dispara em 7 direções simultâneas em um padrão de leque, destruindo muitos inimigos por vez.

---

### 💥 Tipos de Inimigos

#### 🟢 Inimigo Normal (Verde)
```
┌────┐
│░░░░│
└────┘
```
- Movimento: Lateral + Descida
- Ataque: Tiro raro
- Pontos: 100 por destruição

#### 🟣 Inimigo Atirador (Magenta)
```
┌────┐
│◉◉◉◉│
└────┘
```
- Movimento: Lateral + Descida
- Ataque: **Dispara frequentemente** em você
- Pontos: 100 por destruição
- Chance: ~20% por linha

---

### 👹 Chefes (Boss)

Aparecem a cada **5 ondas** completadas (Onda 5, 10, 15, etc)

```
┌──────────────────┐
│    ▰ BOSS ▰      │
│ ◉▰▰▰▰▰▰▰▰▰▰▰◉   │
└──────────────────┘
```

**Características**:
- HP: `50 + (Wave × 15)` (escala com dificuldade)
- Movimento: Ziguezague horizontal
- Ataque: Aumenta com fases de vida

**Fases**:
- 🟢 **Fase 1** (100-70% HP): Disparo único
- 🟡 **Fase 2** (70-30% HP): 3 disparos (padrão)
- 🔴 **Fase 3** (30-0% HP): 5 disparos (padrão ofensivo)

**Recompensa**: 2000 pontos + Acesso ao menu de upgrades

---

### 🎁 PowerUps

Caem aleatoriamente dos inimigos destruídos (~15% de chance)

#### ⚡ **SPEED** (Verde)
```
⚡
```
**Efeito**: Nave 1.6× mais rápida por 7 segundos  
**Cor**: Verde brilhante (#1eff00)

#### 🔥 **MULTI** (Amarelo)
```
🔥
```
**Efeito**: Dispara em 3 direções (esquerda, centro, direita) por 6 segundos  
**Cor**: Amarelo (#ffea00)

#### 🛡️ **SHIELD** (Ciano)
```
🛡️
```
**Efeito**: Ativa escudo protetor por 5 segundos  
**Cor**: Ciano (#00fbff)

---

### 📊 Sistema de Ondas

```
Onda 1-4:   Inimigos normais, dificuldade escala
            ↓
Onda 5:     BOSS FASE 1 (50 HP)
            ↓
Onda 6-9:   Mais inimigos, mais atiradores
            ↓
Onda 10:    BOSS FASE 2 (200 HP)
            ↓
... (padrão continua)
```

**Progressão de Dificuldade**:
- Velocidade dos inimigos aumenta: `110 + (wave × 10)` pixels/s
- Número de linhas aumenta: `min(6, 2 + (wave ÷ 3))`
- Taxa de disparo inimiga aumenta com fase

---

### 📈 Sistema de Upgrades

Após completar cada onda (não-boss), escolha 3 upgrades aleatórios de 4 possíveis:

| Upgrade | Efeito | Impacto |
|---------|--------|--------|
| **DANO +20%** | Multiplica dano por 1.2 | Destruir inimigos 20% mais rápido |
| **VELOCIDADE +15%** | Multiplica velocidade por 1.15 | Esquivar 15% mais fácil |
| **TIRO RÁPIDO** | Reduz delay para 80% | Dispara até 25% mais rápido |
| **REPARAR ESCUDO** | Restaura +0.5 HP máximo | Ganha mais resistência |

**Estratégia**:
- Início: Escolha **VELOCIDADE** para esquivar melhor
- Meio: Equilíbrio entre **DANO** e **VELOCIDADE**
- Final: Priorize **DANO** e **TIRO RÁPIDO** para destruir bosses

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Propósito | Versão |
|-----------|-----------|----------|--------|
| **Linguagem** | Python | Lógica e automação | 3.8+ |
| **GUI** | CustomTkinter | Interface e sidebar | Latest |
| **Renderização 2D** | Tkinter Canvas | Motor gráfico | Nativo |
| **Temporização** | time.perf_counter() | Delta time preciso | Nativo |
| **Persistência** | JSON | Salvar high score | Nativo |
| **Áudio** | Pygame Mixer | Efeitos sonoros | Optional |
| **Estrutura** | Dataclasses | Skins de naves | Nativo (Python 3.7+) |

### Por que essas tecnologias?

- ✅ **CustomTkinter**: Interface moderna que não parecer retro
- ✅ **Canvas Tkinter**: Renderização rápida e responsiva em 2D
- ✅ **time.perf_counter()**: Precisão de microsegundos para physics
- ✅ **JSON**: Leve e portável para salvar dados
- ✅ **Pygame (opcional)**: Áudio profissional sem compilação

---

## 🏗️ Arquitetura e Estrutura

### 📊 Fluxo de Dados

```
┌────────────────────────┐
│   NeonInvaders (Main)  │
│   - UI Management      │
│   - Game Loop          │
│   - Rendering          │
└────────────┬───────────┘
             │
    ┌────────┴─────────┐
    │                  │
┌───▼──┐        ┌─────▼───┐
│Logic │        │ Entities│
│Update│        │(Player, │
│      │        │ Enemies)│
└──────┘        └─────────┘
```

### 🧩 Componentes Principais

```
space.py
│
├── 🎨 CONSTANTES
│   ├── CANVAS_W/H ........... Dimensões (900x800)
│   ├── WINDOW_W/H ......... Janela total (1200x850)
│   ├── SAVE_FILE ......... Onde salva score
│   ├── DROP_TYPES ........ Tipos de power-ups
│   └── UPGRADES ......... Upgrades disponíveis
│
├── 🛸 ESTRUTURAS DE DADOS
│   ├── @dataclass Skin ... Define atributos de nave
│   ├── SKINS{} .......... 3 skins pré-definidas
│   └── class Player .... Estado da nave
│
├── 🎮 CLASSE: NeonInvaders (Controller + View)
│   │
│   ├── INICIALIZAÇÃO
│   │   ├── __init__() .......... Setup inicial
│   │   ├── _setup_ui() ........ Constrói interface
│   │   └── _bind_keys() ...... Mapeia controles
│   │
│   ├── MENUS
│   │   ├── _open_skin_menu() . Menu de seleção
│   │   ├── _select_skin_ui() . Preview da nave
│   │   ├── _open_upgrade_menu() Menu pós-onda
│   │   └── _apply_upgrade() .. Aplica upgrade
│   │
│   ├── CONTROLE DO JOGO
│   │   ├── _start_game() ...... Inicia novo jogo
│   │   ├── _spawn_logic() .... Prepara onda
│   │   ├── _spawn_enemies() .. Cria inimigos
│   │   ├── _spawn_boss() .... Cria chefe
│   │   └── _game_over() ..... Encerra jogo
│   │
│   ├── LÓGICA DE UPDATE
│   │   ├── _update_logic(dt) . Atualiza física
│   │   ├── _update_player_movement() . Movimento
│   │   ├── _update_player_shoot() .... Disparo
│   │   ├── _update_special() . Poder especial
│   │   ├── _update_boss(dt) . IA do chefe
│   │   ├── _update_enemies(dt) .. Inimigos
│   │   ├── _update_bullets(dt) ... Colisões
│   │   ├── _update_particles() ... Efeitos
│   │   ├── _update_drops(dt) ... Power-ups
│   │   ├── _update_specials(dt) Efeitos ativos
│   │   └── _check_wave_clear() . Verifica vitória
│   │
│   ├── RENDERIZAÇÃO
│   │   ├── _draw() ........... Loop de render
│   │   ├── _draw_stars() .... Fundo animado
│   │   ├── _draw_player() ... Nave do jogador
│   │   ├── _draw_enemies() .. Hordas
│   │   ├── _draw_boss() .... Chefe
│   │   ├── _draw_bullets() . Disparos
│   │   ├── _draw_drops() ... PowerUps
│   │   ├── _draw_specials() Escudos/Beams
│   │   └── _draw_messages() . HUD
│   │
│   ├── GAME LOOP
│   │   ├── _game_loop() .... Loop principal (60 FPS)
│   │   └── dt (Delta Time) . Temporal diferencial
│   │
│   └── UTILITÁRIOS
│       ├── _spawn_particles() Efeitos visuais
│       ├── _play_sound() .... Áudio
│       ├── _save/load_progress() Persistência
│       └── _init_stars() .... Background animado
```

---

## 📚 Documentação das Classes Principais

### 1️⃣ `Skin` — Definição de Nave

**Tipo**: `@dataclass`  
**Responsabilidade**: Descrever visualmente e mecanicamente uma nave

**Atributos**:

```python
@dataclass
class Skin:
    name: str              # "Interceptor", "Tanker", etc.
    color: str             # Cor hexadecimal (#00D4FF)
    points: list[tuple]    # Vértices do polígono [(x, y), ...]
    power: str             # "BEAM", "SHIELD", "FAN_SHOT"
    max_hp: float = 1.0    # Pontos de vida máximo
    damage: float = 1.0    # Multiplicador de dano
    fire_rate: float = 0.25 # Delay mínimo entre tiros (segundos)
    speed: float = 520     # Pixels/segundo
```

**Exemplo**:

```python
Interceptor = Skin(
    name="Interceptor",
    color="#00D4FF",
    points=[(0, -20), (-15, 15), (15, 15)],  # Triângulo
    power="BEAM",
    fire_rate=0.15,
    speed=600,
)
```

---

### 2️⃣ `Player` — Estado da Nave

**Responsabilidade**: Manter dados da nave controlada pelo jogador

**Atributos**:

```python
class Player:
    skin: Skin             # Referência à skin
    max_hp: float          # HP máximo
    hp: float              # HP atual
    damage: float          # Dano multiplicador
    fire_rate: float       # Taxa de disparo
    speed: float           # Velocidade
    special: str           # Tipo de poder
    x: float               # Posição X (pixels)
    y: float               # Posição Y (pixels)
```

**Operações**:

```python
# Criar jogador
player = Player(SKINS["Interceptor"])

# Acessar atributos
print(player.x, player.y)        # 450, 650
print(player.hp)                 # 1.0
print(player.special)            # "BEAM"

# Modificar (após upgrade)
player.damage *= 1.2             # +20% dano
player.speed *= 1.15             # +15% velocidade
```

---

### 3️⃣ `NeonInvaders` — Classe Principal

**Responsabilidade**: Gerenciar todo o jogo (UI, lógica, renderização)

#### Método: `_game_loop()`

**Propósito**: Loop principal que roda a ~60 FPS

```python
def _game_loop(self):
    if not self.running:
        return
    
    now = time.perf_counter()
    dt = now - self._last_time  # Delta time em segundos
    self._last_time = now
    
    self._update_logic(dt)      # Atualiza física
    self._draw()                # Renderiza tudo
    
    self.after(16, self._game_loop)  # ~60 FPS (1000/60 ≈ 16ms)
```

---

#### Método: `_update_logic(dt)`

**Propósito**: Atualiza todo o estado do jogo

**Fluxo**:

```python
def _update_logic(self, dt: float):
    # 1. Efeitos visuais
    self._update_shake(dt)              # Screen shake
    self._update_stars(dt)              # Parallax background
    
    # 2. Powerups ativos
    self._update_powerup_timers(dt)     # Countdown SPEED/MULTI
    
    # 3. Entrada do jogador
    self._update_player_movement(dt)    # Ler keys
    self._update_player_shoot()         # Disparar
    self._update_special()              # Poder especial
    
    # 4. IA dos inimigos
    if self.boss_active:
        self._update_boss(dt)           # Lógica do chefe
    else:
        self._update_enemies(dt)        # Lógica dos inimigos normais
    
    # 5. Física
    self._update_player_bullets(dt)     # Mover + Colisões
    self._update_enemy_bullets(dt)      # Mover + Colisões com player
    self._update_particles()            # Partículas (explosões)
    self._update_drops(dt)              # PowerUps caindo
    self._update_specials(dt)           # Escudos/Beams ativos
    
    # 6. Checkpoints
    self._cleanup_barriers()            # Remove barreiras destruídas
    self._check_wave_clear()            # Verifica se onda terminou
    
    # 7. UI atualiza
    self.special_bar.set(self.special_charge)
    self.hp_bar.set(self.player.hp / self.player.max_hp)
```

---

#### Método: `_update_player_movement(dt)`

**Propósito**: Move nave baseado em input

```python
def _update_player_movement(self, dt: float):
    # Velocidade aumentada se tiver SPEED powerup
    spd = self.player.speed * (1.6 if self.active_powerups["SPEED"] > 0 else 1.0)
    
    # Esquerda
    if self.keys["left"] and self.player.x > 40:
        self.player.x -= spd * dt
    
    # Direita
    if self.keys["right"] and self.player.x < CANVAS_W - 90:
        self.player.x += spd * dt
```

**Física**: `posição += velocidade × delta_time`

---

#### Método: `_update_enemies(dt)`

**Propósito**: Move inimigos e faz IA

```python
def _update_enemies(self, dt: float):
    move_down = False
    
    # Movimento horizontal
    for e in self.enemies:
        e["x"] += (110 + self.wave * 10) * dt * self.enemy_direction
        
        # Verifica se chegou no limite
        if (e["x"] > 820 and self.enemy_direction == 1) or \
           (e["x"] < 30 and self.enemy_direction == -1):
            move_down = True
        
        # Atirador? Dispara mais frequentemente
        fire_chance = 0.015 if e["type"] == "SHOOTER" else 0.004
        if random.random() < fire_chance:
            self.enemy_bullets.append({
                "x": e["x"] + 20,
                "y": e["y"] + 30,
                "vx": 0
            })
    
    # Se alguém atingiu limite, desce e muda direção
    if move_down:
        self.enemy_direction *= -1
        for e in self.enemies:
            e["y"] += 35
```

**Velocidade escala**: `110 + (wave × 10)` pixels/s

---

#### Método: `_activate_special()`

**Propósito**: Ativa poder especial baseado em skin

```python
def _activate_special(self):
    self.special_charge = 0.0
    self._play_sound("special")
    
    if self.player.special == "BEAM":
        # INTERCEPTOR: Laser contínuo por 2s
        self.specials.append({"type": "BEAM", "timer": 2.0})
    
    elif self.player.special == "SHIELD":
        # TANKER: Escudo protetor por 6s
        self.specials.append({"type": "SHIELD", "timer": 6.0})
    
    elif self.player.special == "FAN_SHOT":
        # V-STINGER: Dispara em 7 direções
        for vx in range(-300, 301, 100):  # -300, -200, -100, 0, 100, 200, 300
            self.bullets.append({
                "x": self.player.x,
                "y": self.player.y,
                "vx": vx
            })
```

---

## 🎯 Conceitos-Chave Explicados

### 1️⃣ **Delta Time (dt)** — Física Independente de FPS

O problema: Se você fizer `x += velocidade`, o movimento será diferente em PCs rápidos vs. lentos.

**Solução**: Multiplicar por `dt` (tempo decorrido)

```python
# ❌ SEM delta time
player.x += 100  # Pula 100 pixels a cada frame
# Em 60 FPS: 100 × 60 = 6000 pixels/segundo
# Em 30 FPS: 100 × 30 = 3000 pixels/segundo ← Diferente!

# ✅ COM delta time
player.x += 520 * dt  # 520 pixels/segundo em qualquer FPS
# Em 60 FPS: 520 × (1/60) = 8.67 pixels/frame
# Em 30 FPS: 520 × (1/30) = 17.33 pixels/frame
# Velocidade é sempre 520 pixels/segundo! ✓
```

---

### 2️⃣ **Sistema de Partículas** — Efeitos Visuais

Quando inimigo é destruído, cria partículas que se dispersam:

```python
def _spawn_particles(self, x: float, y: float, color: str):
    for _ in range(5):
        self.particles.append({
            "x": x,
            "y": y,
            "vx": random.uniform(-3, 3),     # Velocidade X aleatória
            "vy": random.uniform(-3, 3),     # Velocidade Y aleatória
            "life": 1.0,                     # Durável 1 segundo
            "color": color,                  # Cor da partícula
        })

# No update, cada partícula se move e desaparece
def _update_particles(self):
    for p in self.particles[:]:
        p["x"] += p["vx"]
        p["y"] += p["vy"]
        p["life"] -= 0.05              # Desaparece gradualmente
        if p["life"] <= 0:
            self.particles.remove(p)
```

**Resultado**: Explosão que parece "realista"

---

### 3️⃣ **Screen Shake** — Feedback Tátil Visual

Quando você recebe dano, a câmera treme:

```python
def _update_shake(self, dt: float):
    if self.shake_intensity > 0:
        self.shake_intensity -= 15 * dt  # Diminui gradualmente

# Na renderização, aplicamos offset aleatório:
ox = random.uniform(-self.shake_intensity, self.shake_intensity)
oy = random.uniform(-self.shake_intensity, self.shake_intensity)

# Tudo é desenhado com este offset:
self.canvas.create_polygon(pts, ...)  # Desenha no (x+ox, y+oy)
```

**Efeito**: Câmera tremendo quando recebe impacto

---

### 4️⃣ **Powerups e Timers** — Gerencimento Temporal

Powerups não são permanentes, eles têm duração:

```python
# Coletou powerup
self.active_powerups["SPEED"] = 7.0  # Ativo por 7 segundos

# Na renderização, aplicamos multiplier se ativo
spd = self.player.speed * (1.6 if self.active_powerups["SPEED"] > 0 else 1.0)

# No update, countdown
def _update_powerup_timers(self, dt: float):
    for k in self.active_powerups:
        if self.active_powerups[k] > 0:
            self.active_powerups[k] -= dt
```

**Resultado**: Efeito por tempo limitado e previsível

---

### 5️⃣ **Sistema de Fases do Boss** — Escalação de Dificuldade

Boss muda de comportamento conforme leva dano:

```python
def _update_boss(self, dt: float):
    hp_ratio = self.boss_hp / self.boss_max_hp
    
    # Defina fase por HP
    if hp_ratio < 0.3:       # Menos de 30% HP
        self.boss_phase = 3  # MUITO OFENSIVO
    elif hp_ratio < 0.7:     # Menos de 70% HP
        self.boss_phase = 2  # OFENSIVO
    else:                    # Mais de 70% HP
        self.boss_phase = 1  # DEFENSIVO
    
    # Velocidade aumenta com fase
    speed = 220 + self.boss_phase * 50
    self.boss_x += speed * dt * self.boss_dir
    
    # Número de disparos aumenta com fase
    fire_chance = 0.05 + self.boss_phase * 0.03
    if random.random() < fire_chance:
        if self.boss_phase == 1:
            vxs = [0]                     # 1 tiro
        elif self.boss_phase == 2:
            vxs = [-150, 0, 150]          # 3 tiros
        else:
            vxs = [-250, -120, 0, 120, 250]  # 5 tiros
```

**Progresso**: Boss fica progressivamente mais agressivo

---

### 6️⃣ **Colisão Retângulo** — Hit Detection

Verificar se bala atingiu inimigo:

```python
def _check_bullet_hits_enemy(self, b: dict):
    for e in self.enemies[:]:
        # Bounding box collision
        if e["x"] < b["x"] < e["x"] + 40 and \
           e["y"] < b["y"] < e["y"] + 35:
            # HIT!
            self.enemies.remove(e)
            self.score += 100
            self.bullets.remove(b)
            break
```

**Lógica**: Se bala está dentro do retângulo do inimigo → Colisão!

---

## 📊 Fluxo Completo de Jogo

```
1. Inicializa aplicação
   NeonInvaders()
   ↓
2. Mostra menu de seleção de nave
   _open_skin_menu()
   ├─ Preview da nave
   └─ Botões: Interceptor, Tanker, V-Stinger
   ↓
3. Usuário escolhe nave e clica DECOLAR
   _start_game()
   ├─ Cria Player com skin selecionada
   ├─ Reseta score, wave = 1
   ├─ Cria barreiras
   └─ Chama _spawn_logic()
   ↓
4. Spawn de inimigos (Onda 1)
   _spawn_enemies()
   ├─ Cria 2 linhas de 8 inimigos
   └─ ~20% são SHOOTERS
   ↓
5. GAME LOOP (60 FPS)
   ┌─────────────────────┐
   │ _update_logic(dt)   │
   │ ├─ Entrada         │
   │ ├─ Física          │
   │ ├─ Colisões        │
   │ └─ Lógica          │
   │                     │
   │ _draw()            │
   │ ├─ Stars           │
   │ ├─ Nave            │
   │ ├─ Inimigos        │
   │ └─ Efeitos         │
   └─────────────────────┘
          ↓ (até inimigos = 0)
   ↓
6. Onda Completa
   _check_wave_clear()
   ├─ Limpa tela
   └─ Wave += 1
   ↓
7. Wave % 5 == 0?
   ├─ SIM → Boss battle (wave 5, 10, 15...)
   │        └─ Após vencer: Menu de upgrades
   └─ NÃO → Próxima onda (volta ao passo 5)
   ↓
8. Jogador é atingido múltiplas vezes
   player.hp <= 0
   ↓
9. Game Over
   _game_over()
   ├─ Salva high score se bateu recorde
   └─ Volta ao passo 2 (menu)
```

---

## 🎨 Sistema de Cores

Paleta **cyberpunk/neon** com tons brilhantes:

```python
# Naves
Interceptor: #00D4FF (Ciano brilhante)
Tanker:      #FFD700 (Ouro)
V-Stinger:   #FF0055 (Rosa quente)

# Inimigos
Normal:      #00FF9C (Verde neon)
Shooter:     #FF00FF (Magenta)
Boss:        #FF0000 (Vermelho puro)

# Efeitos
Shield:      #00fbff (Ciano claro)
Beam:        #00D4FF (Ciano branco)
Barrier:     #00ff9c (Verde escuro)
Particles:   Variadas (explosões coloridas)

# UI
Background:  #000000 (Preto absoluto)
Sidebar:     #080808 (Preto suave)
Text:        #FFFFFF (Branco)
```

---

## 💾 Persistência de Dados

O jogo salva o **high score** automaticamente:

```python
# Salvar
def _save_progress(self):
    with open("save_data.json", "w") as f:
        json.dump({"high_score": self.high_score}, f)

# Carregar na inicialização
def _load_progress(self):
    if os.path.exists("save_data.json"):
        with open("save_data.json", "r") as f:
            self.high_score = json.load(f).get("high_score", 0)
```

**Arquivo gerado**: `save_data.json`

```json
{
    "high_score": 45000
}
```

---

## 🔊 Sistema de Áudio (Opcional)

O jogo suporta som via **Pygame Mixer**, mas é opcional:

```python
try:
    import pygame
    pygame.mixer.init()
    SOUND_ENABLED = True
except ImportError:
    SOUND_ENABLED = False

# Para tocar som:
def _play_sound(self, name: str):
    if SOUND_ENABLED:
        try:
            pygame.mixer.Sound(f"sounds/{name}.wav").play()
        except Exception:
            pass  # Arquivo não encontrado, ignora
```

**Sons usados**:
- `shoot.wav` — Disparo
- `explosion.wav` — Inimigo destruído
- `hit.wav` — Nave atingida
- `upgrade.wav` — Coletou powerup
- `special.wav` — Ativou poder especial

Para ativar: crie pasta `sounds/` com esses `.wav` files

---

## 🛑 Barreiras Destrutíveis

Elementos defensivos que bloqueiam disparos:

```python
def _create_barriers(self):
    self.barriers = [
        {"x": 150 + i * 200, "y": 550, "hp": 10, "w": 80, "h": 15}
        for i in range(4)
    ]
```

**Características**:
- 4 barreiras na base (Y=550)
- 10 HP cada (absorve 10 tiros)
- Bloqueiam tanto suas balas quanto as inimigas
- Desaparecem quando HP ≤ 0

---

## 🚀 Possíveis Melhorias Futuras

- [ ] **Mais Naves**: Adicionar 5+ skins com mecânicas únicas
- [ ] **Sistema de Combos**: Bônus por eliminar múltiplos inimigos
- [ ] **Efeitos de Câmera**: Zoom e rotação
- [ ] **Tutorial Interativo**: Explicar controles
- [ ] **Leaderboard Online**: Competição com outros jogadores
- [ ] **Modos de Jogo**: Survival, Time Attack, Story Mode
- [ ] **Inimigos Especiais**: Elite enemies com padrões únicos
- [ ] **Boss de Fase**: Boss mais forte a cada 10 ondas
- [ ] **Achievements/Conquistas**: Desbloqueáveis
- [ ] **Configurações**: Volume, dificuldade, controles customizados

---

## 🐛 Troubleshooting Avançado

### ❌ Problema: "ModuleNotFoundError: customtkinter"
**Solução**: `pip install customtkinter`

### ❌ Problema: Jogo lagado
**Causas possíveis**:
- Muito código rodando fora do game loop
- `_draw()` desenhando muitos elementos

**Solução**:
- Reduza número de partículas
- Use `delete("all")` ao invés de redesenhar partes individuais

### ❌ Problema: Sons não funcionam
**Causa**: Pygame não instalado ou arquivos não encontrados  
**Solução**: 
```bash
pip install pygame
# E coloque arquivos .wav em pasta "sounds/"
```

### ❌ Problema: Nave desaparece da tela
**Causa**: Possível y fora de limites  
**Verificação**:
```python
print(f"Player X: {self.player.x}, Y: {self.player.y}")
print(f"Canvas: {CANVAS_W}x{CANVAS_H}")
```

---

## 📋 Instalação e Execução

### ✅ Pré-requisitos

- Python 3.8+
- pip

### 🔧 Passos

1. **Clone o repositório**:
```bash
git clone https://github.com/luisguigui/space-invaders.git
cd space-invaders
```

2. **Crie ambiente virtual** (opcional mas recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Instale dependências**:
```bash
pip install customtkinter
# Opcional para som:
pip install pygame
```

4. **Execute o jogo**:
```bash
python space.py
```

5. **Menu de seleção de nave vai aparecer**:
   - Escolha sua nave (Interceptor, Tanker ou V-Stinger)
   - Clique em **DECOLAR**
   - Divirta-se! 🚀

---

## ⚙️ Configuração Avançada

### Modificar Constantes

Edite o arquivo `space.py` para ajustar:

```python
# Tamanho da janela
CANVAS_W = 900
CANVAS_H = 800
WINDOW_W = 1200
WINDOW_H = 850

# Arquivo de save
SAVE_FILE = "save_data.json"

# Tipos de power-ups (adicionar novo):
DROP_TYPES = {
    "SPEED":  {"color": "#1eff00", "label": "⚡"},
    "SHIELD": {"color": "#00fbff", "label": "🛡️"},
    "MULTI":  {"color": "#ffea00", "label": "🔥"},
    # Seu novo powerup aqui:
    # "LASER": {"color": "#ff0000", "label": "🔴"},
}

# Upgrades disponíveis (adicionar novo):
UPGRADES = [
    {"name": "DANO +20%", "effect": "damage"},
    {"name": "VELOCIDADE +15%", "effect": "speed"},
    {"name": "TIRO RÁPIDO", "effect": "firerate"},
    {"name": "REPARAR ESCUDO", "effect": "hp"},
    # Seu novo upgrade:
    # {"name": "CRIT +10%", "effect": "crit"},
]
```

### Criar Nova Nave

```python
SKINS = {
    # ... (skins existentes)
    
    "MísseisSensor": Skin(
        name="MísseisSensor",
        color="#FF6600",
        points=[(0, -10), (-8, 10), (8, 10), (0, 0)],
        power="HOMING",  # Novo tipo de poder
        fire_rate=0.20,
        speed=550,
        damage=2.5,
        max_hp=1.5,
    ),
}
```

---

## 🤝 Colaboradores

- 👤 **Luis Guilherme G.B.** — Desenvolvimento principal
- 👤 **Otavio Cesar** — Co-desenvolvimento

Desenvolvido como projeto educacional focado em:
- Física de jogo em tempo real
- Padrões de design em jogos
- Otimização de performance

---

## ✒️ Autor

**Luis Guilherme G.B.**

- 🐙 GitHub: [@luisguigui](https://github.com/luisguigui)
- 💼 Portfólio: Desenvolvedor Python Full-Stack
- 📧 Contato: Abra uma issue no repositório

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Use, modifique e distribua livremente!

---

## 🌟 Se gostou, considere dar uma ⭐!

Seu feedback é importante! Abra issues com sugestões, bugs ou novas ideias.

```
        ⭐
       ⭐⭐⭐
      ⭐⭐⭐⭐⭐
   OBRIGADO PELO SUPORTE!
```

---

**Última atualização**: 2026-04-20  
**Versão**: 1.0 — Stable Release  
**Status**: ✅ Totalmente funcional e jogável
```

---
