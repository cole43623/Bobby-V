TEMPO = 0.2

from game_classes import LAST_LEVEL, TILE_SIZE
import time
import importlib
init_map = []
for i in range(LAST_LEVEL):
    module = importlib.import_module(f'liv{i}')
    init_map.append(getattr(module, f'init_map{i}'))


def put_image_to_image(game, img, x_off, y_off):
    game.screen.blit(img, (x_off, y_off))

def draw_map(self):
    for i in range(self.lenrow):
        for j in range(self.lencol):
            tile = self.layout[i][j]
            #img = self.images[tile]
            if tile == 'E' and self.number_coin == 0:
                img = self.end_images[self.frame_end]
            elif tile == '1':
                img = self.belt_left_images[self.frame_end]
            elif tile == '2':
                img = self.belt_right_images[self.frame_end]
            elif tile == '3':
                img = self.belt_up_images[self.frame_end]
            elif tile == '4':
                img = self.belt_down_images[self.frame_end]
            else:
                img = self.images[tile]
            put_image_to_image(self, img, j*TILE_SIZE, i*TILE_SIZE)
    put_image_to_image(self, self.player_images[self.direction - 1], self.player_pos[0], self.player_pos[1])

def is_end(self):
    px, py = self.player_pos
    # morte
    if self.layout[int((py+10)/TILE_SIZE)][int((px+5)/TILE_SIZE)] == 'S' or self.layout[int((py+10)/TILE_SIZE)][int((px+25)/TILE_SIZE)] == 'S':
        self.death_sound.play()
        print("dead")
        self.tot_dead += 1
        init_map[self.liv](self)
        time.sleep(0.5)
        draw_map(self)
    # vittoria
    elif self.number_coin == 0 and (self.layout[int((py+13)/TILE_SIZE)][int((px+5)/TILE_SIZE)] == 'E' or self.layout[int((py+13)/TILE_SIZE)][int((px+25)/TILE_SIZE)] == 'E'):
        self.win_sound.play()
        print("win")
        self.end = True

def update_player(self, key):
    px, py = self.player_pos
    x_idx = int(px / TILE_SIZE)
    y_idx = int(py / TILE_SIZE)
    flag = False

    if key == 1: # LEFT
        if x_idx > 0 and self.layout[y_idx][x_idx - 1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0167" and self.layout[y_idx][x_idx] not in "567":
            flag = True
            self.player_pos[0] -= 32
    elif key == 2: # RIGHT
        if x_idx < self.lencol - 1 and self.layout[y_idx][x_idx + 1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0289"  and self.layout[y_idx][x_idx] not in "589":
            flag = True
            self.player_pos[0] += 32
    elif key == 3: # UP
        if y_idx > 0 and self.layout[y_idx - 1][x_idx] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ3578" and self.layout[y_idx][x_idx] not in "078":
            self.player_pos[1] -= 32
            flag = True
    elif key == 4: # DOWN
        if y_idx < self.lenrow - 1 and self.layout[y_idx + 1][x_idx] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ4569" and self.layout[y_idx][x_idx] not in "069":
            self.player_pos[1] += 32
            flag = True
    if self.layout[self.player_pos[1]//32][self.player_pos[0]//32] == 'C':
        self.layout[self.player_pos[1]//32][self.player_pos[0]//32] = 'H'
        self.number_coin -= 1

    if flag:
        if self.layout[y_idx][x_idx] == 'T':
            self.layout[y_idx][x_idx] = 'S'
        elif self.layout[y_idx][x_idx] == '5':
            self.layout[y_idx][x_idx] = '0'
        elif self.layout[y_idx][x_idx] == '0':
            self.layout[y_idx][x_idx] = '5'
        elif self.layout[y_idx][x_idx] in "6789":
            self.layout[y_idx][x_idx] = str((int(self.layout[y_idx][x_idx]) - 5) % 4 + 6)
    is_end(self)

def check_belt(self):
    px, py = self.player_pos
    x_idx = int(px / TILE_SIZE)
    y_idx = int(py / TILE_SIZE)
    tile = self.layout[y_idx][x_idx]
    
    if tile in "1234":
        update_player(self, int(tile))
        self.direction = int(tile)
        return True
    return False

def key_press(self, key):
    px, py = self.player_pos
    if self.layout[py // TILE_SIZE][px // TILE_SIZE] in "1234":
        return

    if key in [97, 1073741904]:
        self.direction = 1
        update_player(self, 1)
    elif key in [100, 1073741903]:
        self.direction = 2
        update_player(self, 2)
    elif key in [119, 1073741906]:
        self.direction = 3
        update_player(self, 3)
    elif key in [115, 1073741905]:
        self.direction = 4
        update_player(self, 4)
    elif key == 27:
        exit(0)
