
def init_map39(game):
    game.moving_left = 0
    game.moving_right = 0
    game.player_pos[0] = 1 * 32
    game.player_pos[1] = 1 * 32
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
aaaaaaaaaaaaaaaaaaadaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaakZgaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaak*gaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaak+gaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaddd5dadddaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaakE]JJJ0-/Zgaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaljJAJelllaaaaaaaaaaaaaaa
aaaaaaaaaaaaaddddhJJJJeddddaaaaaaaaaaaaa
aaaaaaaaaaaakJJJJJ4mm3JJJJmgaaaaaaaaaaaa
aaaaaaaaaaaakJJJJJJmmJJJm5mgaaaaaaaaaaaa
aaaaaaaaaaaakm5m5m5mm5m5m+mgaaaaaaaaaaaa
aaaaaaaaaaaakm+m+m-mm+m-m/mgaaaaaaaaaaaa
aaaaaaaaaaaakm*mZmZmmZm*m[mgaaaaaaaaaaaa
aaaaaaaaaaaakrqqqqqqqqoZrqogaaaaaaaaaaaa
aaaaaaaaaaaaallllllllllllllaaaaaaaaaaaaa
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
                game.player_pos[0] = j * 32
                game.player_pos[1] = i * 32