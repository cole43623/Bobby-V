from game_classes import TILE_SIZE

def init_map17(game):
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
aaaaaaaaaaaaaaaaaaaadddaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaadddkJJJgdddaaaaaaaaaaaaa
aaaaaaaaaaaaaaakCCC}JJJ]CCCgaaaaaaaaaaaa
aaaaaaaaaaaaaaakCCCgjJfkCCCgaaaaaaaaaaaa
aaaaaaaaaaaaaaaalccdh-edcccaaaaaaaaaaaaa
aaaaaaaaaaaaadddhJJJJJJJJJJgaaaaaaaaaaaa
aaaaaaaaaaaakJJ+-JJ708b708Jgaaaaaaaaaaaa
aaaaaaaaaaaakmJJJJJ5[9b6{5Jgaaaaaaaaaaaa
aaaaaaaaaaaakmCCCJJ6000009Jgaaaaaaaaaaaa
aaaaaaaaaaaakmCCCmJJJJJJJJJgaaaaaaaaaaaa
aaaaaaaaaaaakro)rofccclllllaaaaaaaaaaaaa
aaaaaaaaaaaaajJJJfkJJJgdaaaaaaaaaaaaaaaa
aaaaaaaaaaaaakJAJehJ(J0Egaaaaaaaaaaaaaaa
aaaaaaaaaaaaakJJJJJJJJglaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaallllllllaaaaaaaaaaaaaaaaaa
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