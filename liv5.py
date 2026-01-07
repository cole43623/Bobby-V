from game_classes import TILE_SIZE

def init_map5(game):
    game.moving_left = 0
    game.moving_right = 0
    game.player_pos[0] = 15 * TILE_SIZE
    game.player_pos[1] = 16 * TILE_SIZE
    game.y_velocity = 0
    game.jumping = 0
    game.jolly[0] = 0
    game.jolly[1] = 0
    game.end = 0

    map_data = """\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaadddaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaadddadhJJJgaaaaaaaaaaaaaaa
aaaaaaaaaaaaaakCJJTJJJEJgaaaaaaaaaaaaaaa
aaaaaaaaaaaaaakJflaljJJJgaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaTaadddcTcdddaaaaaaaaaaaaa
aaaaaaaaaaaaaakJehCCJJJJJCCgaaaaaaaaaaaa
aaaaaaaaaaaaaakCJJCCJrqoJCCgaaaaaaaaaaaa
aaaaaaaaaaaaaaalljCCJJJJJCCgaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaallTcccTllaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaakCTTTCgaaaaaaaaaaaaaa
aaaaaaaaaaaaaadddaadTcccTdaaaaaaaaaaaaaa
aaaaaaaaaaaaakJJJehJJCCCJJgaaaaaaaaaaaaa
aaaaaaaaaaaaakJAJJJJJCTCJJgaaaaaaaaaaaaa
aaaaaaaaaaaaakJJJfjJJCCCJJgaaaaaaaaaaaaa
aaaaaaaaaaaaaalllaalllllllaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
    # map to layout
    game.number_coin = 0
    map_data = map_data.replace("\n", "").replace(" ", "")
    for i in range(game.lenrow):
        for j in range(game.lencol):
            game.layout[i][j] = map_data[i*game.lencol + j]
            if map_data[i*game.lencol + j] in 'ZC':
                game.number_coin += 1