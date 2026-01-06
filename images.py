import pygame
from game_classes import TILE_SIZE

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
    game.images["belt_right1"] = pygame.transform.scale(pygame.image.load("tiles/belt_right_1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_right2"] = pygame.transform.scale(pygame.image.load("tiles/belt_right_2.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_right3"] = pygame.transform.scale(pygame.image.load("tiles/belt_right_3.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_right4"] = pygame.transform.scale(pygame.image.load("tiles/belt_right_4.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_left1"] = pygame.transform.scale(pygame.image.load("tiles/belt_left_1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_left2"] = pygame.transform.scale(pygame.image.load("tiles/belt_left_2.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_left3"] = pygame.transform.scale(pygame.image.load("tiles/belt_left_3.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_left4"] = pygame.transform.scale(pygame.image.load("tiles/belt_left_4.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_up1"] = pygame.transform.scale(pygame.image.load("tiles/belt_up_1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_up2"] = pygame.transform.scale(pygame.image.load("tiles/belt_up_2.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_up3"] = pygame.transform.scale(pygame.image.load("tiles/belt_up_3.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_up4"] = pygame.transform.scale(pygame.image.load("tiles/belt_up_4.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_down1"] = pygame.transform.scale(pygame.image.load("tiles/belt_down_1.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_down2"] = pygame.transform.scale(pygame.image.load("tiles/belt_down_2.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_down3"] = pygame.transform.scale(pygame.image.load("tiles/belt_down_3.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["belt_down4"] = pygame.transform.scale(pygame.image.load("tiles/belt_down_4.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["5"] = pygame.transform.scale(pygame.image.load("tiles/wall_left_right.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["6"] = pygame.transform.scale(pygame.image.load("tiles/wall_left_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["7"] = pygame.transform.scale(pygame.image.load("tiles/wall_left_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["8"] = pygame.transform.scale(pygame.image.load("tiles/wall_right_up.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["9"] = pygame.transform.scale(pygame.image.load("tiles/wall_right_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["0"] = pygame.transform.scale(pygame.image.load("tiles/wall_up_down.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["+"] = pygame.transform.scale(pygame.image.load("tiles/red_button.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["-"] = pygame.transform.scale(pygame.image.load("tiles/red_button_pressed.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["*"] = pygame.transform.scale(pygame.image.load("tiles/yellow_button.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["/"] = pygame.transform.scale(pygame.image.load("tiles/yellow_button_pressed.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["("] = pygame.transform.scale(pygame.image.load("tiles/golden_key.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images[")"] = pygame.transform.scale(pygame.image.load("tiles/golden_lock.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["["] = pygame.transform.scale(pygame.image.load("tiles/silver_key.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["]"] = pygame.transform.scale(pygame.image.load("tiles/silver_lock.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["{"] = pygame.transform.scale(pygame.image.load("tiles/copper_key.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.images["}"] = pygame.transform.scale(pygame.image.load("tiles/copper_lock.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
    game.player_images =  [game.images["left"], game.images["right"], game.images["up"], game.images["down"]]
    game.end_images =  [game.images["E"], game.images["E2"], game.images["E3"], game.images["E4"]]
    game.belt_right_images = [game.images["belt_right1"], game.images["belt_right2"], game.images["belt_right3"], game.images["belt_right4"]]
    game.belt_left_images = [game.images["belt_left1"], game.images["belt_left2"], game.images["belt_left3"], game.images["belt_left4"]]
    game.belt_up_images = [game.images["belt_up1"], game.images["belt_up2"], game.images["belt_up3"], game.images["belt_up4"]]
    game.belt_down_images = [game.images["belt_down1"], game.images["belt_down2"], game.images["belt_down3"], game.images["belt_down4"]]