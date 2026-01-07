import pygame
import sys, os

# main.py
import importlib
init_map = []
from game_classes import GameMap, LAST_LEVEL, TILE_SIZE
for i in range(LAST_LEVEL):  # Numero di livelli
    module = importlib.import_module(f'liv{i}')
    init_map.append(getattr(module, f'init_map{i}'))
from draw import update_player, key_press, draw_map, check_belt
from images import load_images

# =========================
# LOOP PRINCIPALE PER LIVELLI
# =========================
def start_level(game):
    pygame.init()
    game.death_sound = pygame.mixer.Sound("death.wav")
    game.win_sound = pygame.mixer.Sound("win.wav")
    
    # Crea una finestra iniziale
    screen_width = game.lencol * TILE_SIZE
    screen_height = game.lenrow * TILE_SIZE
    game.screen = pygame.display.set_mode((screen_width, screen_height))
    
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
            current_time = pygame.time.get_ticks()
            if current_time - last_anim_time > 200:  # 200ms per frame
                game.frame_end = (game.frame_end + 1) % len(game.end_images)
                check_belt(game)
                last_anim_time = current_time
                draw_map(game)

            pygame.display.flip()

        game.liv += 1
    if (game.cheated):
        print("Usando gli skip")
    print(f"total dead: {game.total_dead}")
    pygame.quit()
    sys.exit()


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    game = GameMap()
    start_level(game)
