
def init_map4(game):
    game.moving_left = 0
    game.moving_right = 0
    game.player_pos[0] = 20 * 32
    game.player_pos[1] = 15 * 32
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
aaaaaaaaaaaaaaaaaaadddaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaddddhJEJeddddaaaaaaaaaaaaa
aaaaaaaaaaaaakTJJJJJJJJJJJTgaaaaaaaaaaaa
aaaaaaaaaaaaakCfllljTfllljCgaaaaaaaaaaaa
aaaaaaaaaaaaakCgaadhCedaakCgaaaaaaaaaaaa
aaaaaaaaaaaaakCedhCCTCCedhCgaaaaaaaaaaaa
aaaaaaaaaaaaakTJJJCCbCCJJJTgaaaaaaaaaaaa
aaaaaaaaaaaaaallljCCTCCflllaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaljJflaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaahJeaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaakJJJgaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaakJAJgaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaakJJJgaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaalllaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
    # map to layout
    map_data = map_data.replace("\n", "").replace(" ", "")
    for i in range(game.lenrow):
        for j in range(game.lencol):
            game.layout[i][j] = map_data[i*game.lencol + j]
            if map_data[i*game.lencol + j] == 'C':
                game.number_coin += 1