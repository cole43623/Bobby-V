from game_classes import TILE_SIZE

def init_map24(game):
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
aaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaahCeaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaTC9CTaddaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaadkCpqnCi78gaaaaaaaaaaaaaaaa
aaaaaaaaaaaakCiCmCmCg55addaaaaaaaaaaaaaa
aaaaaaaaaaaak+i[1+1)g5C0*Cgaaaaaaaaaaaaa
aaaaaaaaaaaaa0ajmJmfa0lal3aaaaaaaaaaaaaa
aaaaaaaaaaaakJehJ9JehJedd3aaaaaaaaaaaaaa
aaaaaaaaaaaakAJJJJJJJEJ]JJgaaaaaaaaaaaaa
aaaaaaaaaaaakJrqo5m0ll5lllaaaaaaaaaaaaaa
aaaaaaaaaaaakJ5J(*mJgaTaaaaaaaaaaaaaaaaa
aaaaaaaaaaaakJrqqqo/gaTaaaaaaaaaaaaaaaaa
aaaaaaaaaaaakJ0+CmCCgkJgaaaaaaaaaaaaaaaa
aaaaaaaaaaaakJrqqnCCehCgaaaaaaaaaaaaaaaa
aaaaaaaaaaaakJ0-CmCC+JCgaaaaaaaaaaaaaaaa
aaaaaaaaaaaaalallllllllaaaaaaaaaaaaaaaaa
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