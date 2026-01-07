from game_classes import TILE_SIZE

def init_map45(game):
    game.moving_left = 0
    game.moving_right = 0
    game.player_pos[0] = 1 * TILE_SIZE
    game.player_pos[1] = 1 * TILE_SIZE
    game.y_velocity = 0
    game.jumping = 0
    game.jolly[0] = 0
    game.jolly[1] = 0
    game.end = 0

    map_data = """\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaddddaaddaaddddaaaaaaaaaaaaa
aaaaaaaaaaaakJJJJgkZZgk*mZZgaaaaaaaaaaaa
aaaaaaaaaaaakJJEJehZZehJJ7Zgaaaaaaaaaaaa
aaaaaaaaaaaakJJJJZZZZ+ZAJJJgaaaaaaaaaaaa
aaaaaaaaaaaakJrqoZZroZZrqoJgaaaaaaaaaaaa
aaaaaaaaaaaakJZZZ11Z{9ZZZZJgaaaaaaaaaaaa
aaaaaaaaaaaakJZ+ZroZZroZZZJgaaaaaaaaaaaa
aaaaaaaaaaaaallj*Z-55ZZ3lllaaaaaaaaaaaaa
aaaaaaaaaaaaaddhZZZ55ZZ3dddaaaaaaaaaaaaa
aaaaaaaaaaaakJZZ(roZZroZZZJgaaaaaaaaaaaa
aaaaaaaaaaaakJZZZ+/ZZ8J-ZZJgaaaaaaaaaaaa
aaaaaaaaaaaakJrqoZZroZZrqoJgaaaaaaaaaaaa
aaaaaaaaaaaakZZZ9ZZ})ZZ8ZZZgaaaaaaaaaaaa
aaaaaaaaaaaakZZZZfjZZfjJZZZgaaaaaaaaaaaa
aaaaaaaaaaaaallllaallaallllaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""
    # map to layout
    game.number_coin = 0
    game.keys = []
    map_data = map_data.replace("\n", "").replace(" ", "")
    for i in range(game.lenrow):
        for j in range(game.lencol):
            game.layout[i][j] = map_data[i*game.lencol + j]
            if map_data[i*game.lencol + j] in 'ZC':
                game.number_coin += 1
            if map_data[i*game.lencol + j] == 'A':
                game.player_pos[0] = j * TILE_SIZE
                game.player_pos[1] = i * TILE_SIZE