import pygame
import sys, os

# main.py
import importlib
init_map = []
from game_classes import GameMap, LAST_LEVEL, TILE_SIZE
for i in range(LAST_LEVEL):  # Numero di livelli
    module = importlib.import_module(f'liv{i}')
    init_map.append(getattr(module, f'init_map{i}'))
from draw import update_player, key_press, draw_map

# =========================
# CARICAMENTO IMMAGINI
# =========================
def load_images(game):
    if game.images:
        return
    game.images["A"] = pygame.transform.scale(pygame.image.load("tiles/start.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["E"] = pygame.transform.scale(pygame.image.load("tiles/end_1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["E2"] = pygame.transform.scale(pygame.image.load("tiles/end_2.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["E3"] = pygame.transform.scale(pygame.image.load("tiles/end_3.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["E4"] = pygame.transform.scale(pygame.image.load("tiles/end_4.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["S"] = pygame.transform.scale(pygame.image.load("tiles/trap_activated.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["T"] = pygame.transform.scale(pygame.image.load("tiles/trap.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["right"] = pygame.transform.scale(pygame.image.load("png/right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["left"] = pygame.transform.scale(pygame.image.load("png/left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["up"] = pygame.transform.scale(pygame.image.load("png/up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["down"] = pygame.transform.scale(pygame.image.load("png/down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["J"] = pygame.transform.scale(pygame.image.load("tiles/ground.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["a"] = pygame.transform.scale(pygame.image.load("tiles/grass.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["C"] = pygame.transform.scale(pygame.image.load("tiles/carrot.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["H"] = pygame.transform.scale(pygame.image.load("tiles/carrot_hole.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["b"] = pygame.transform.scale(pygame.image.load("tiles/grass_down_up_right_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["c"] = pygame.transform.scale(pygame.image.load("tiles/grass_down_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["d"] = pygame.transform.scale(pygame.image.load("tiles/grass_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["e"] = pygame.transform.scale(pygame.image.load("tiles/grass_left_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["f"] = pygame.transform.scale(pygame.image.load("tiles/grass_left_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["g"] = pygame.transform.scale(pygame.image.load("tiles/grass_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["h"] = pygame.transform.scale(pygame.image.load("tiles/grass_right_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["i"] = pygame.transform.scale(pygame.image.load("tiles/grass_right_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["j"] = pygame.transform.scale(pygame.image.load("tiles/grass_right_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["k"] = pygame.transform.scale(pygame.image.load("tiles/grass_right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["l"] = pygame.transform.scale(pygame.image.load("tiles/grass_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["m"] = pygame.transform.scale(pygame.image.load("tiles/fence_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["n"] = pygame.transform.scale(pygame.image.load("tiles/fence_left_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["o"] = pygame.transform.scale(pygame.image.load("tiles/fence_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["p"] = pygame.transform.scale(pygame.image.load("tiles/fence_right_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["q"] = pygame.transform.scale(pygame.image.load("tiles/fence_right_left.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["r"] = pygame.transform.scale(pygame.image.load("tiles/fence_right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.player_images =  [game.images["left"], game.images["right"], game.images["up"], game.images["down"]]
    game.end_images =  [game.images["E"], game.images["E2"], game.images["E3"], game.images["E4"]]
    game.inverted = False

# =========================
# LOOP PRINCIPALE PER LIVELLI
# =========================
def start_level(game):
    pygame.init()
    game.death_sound = pygame.mixer.Sound("death.wav")
    game.win_sound = pygame.mixer.Sound("win.wav")
    
    # Crea una finestra iniziale SOLO per convertire le immagini
    game.screen = pygame.display.set_mode((1280, 704))
    
    load_images(game)  # carica tutte le immagini una volta
     
    while game.liv < LAST_LEVEL:
        # Inizializza la mappa del livello
        init_map[game.liv](game)
        print(f"LEVEL {game.liv + 1}")
        pygame.display.set_caption(f"Game - Level {game.liv + 1}")
        game.end = False
        draw_map(game)
        last_anim_time = pygame.time.get_ticks()
        while not game.end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.end = True
                    game.liv = LAST_LEVEL
                elif event.type == pygame.KEYDOWN:
                    key_press(game, event.key)
            
            # Animazione uscita e refresh mappa se necessario
            if game.number_coin == 0:
                current_time = pygame.time.get_ticks()
                if current_time - last_anim_time > 200:  # 200ms per frame
                    game.frame_end = (game.frame_end + 1) % len(game.end_images)
                    last_anim_time = current_time
                    draw_map(game)

            pygame.display.flip()

        game.liv += 1
    if (game.cheated):
        print("Chi skippa NON può accedere al livello finale.")
    elif (game.total_dead > 99):
        print("Devi fare MENO di 100 morti per accedere al livello finale.")
    print(f"total dead: {game.total_dead}")
    pygame.quit()
    sys.exit()


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    game = GameMap()
    start_level(game)
