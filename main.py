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
from images import load_images

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
