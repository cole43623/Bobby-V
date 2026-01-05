# ==========================
# solong.py  (header Python)
# ==========================


# ==========================
# COSTANTI (equivalenti a #define)
# ==========================
TILE_SIZE = 32
LAST_LEVEL = 7


# ==========================
# CLASSE PRINCIPALE (equivalente di struct t_map)
# ==========================
class GameMap:
    def __init__(self):
        # --- carica i suoni ---
        self.death_sound = None
        self.win_sound = None

        # valori base
        self.path = None
        self.lenrow = 22
        self.lencol = 40
        self.tot_dead = 0
        self.cheated = False
        self.player = 0

        # posizione e movimento
        self.player_pos = [0, 0]
        self.direction = 1
        self.left_speed = -1.2
        self.right_speed = 1.2
        self.jump_velocity = 0.8
        self.number_coin = 0
        self.inverted = False

        # stato gioco
        self.liv = 6
        self.end = 0
        self.frame_end = 0

        # oggetti pygame
        self.screen = None       # pygame display (per mantenere naming simile)
        self.win = None       # pygame window

        # altri dati
        self.jolly = [0.0 for _ in range(100)]
        self.layout = [["" for _ in range(40)] for _ in range(22)]
        self.images = {} 
        self.total_dead = 0  
