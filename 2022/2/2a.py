with open('input.txt', 'r') as input:
    player_score = 0
    won = False
    opponent_moves = ['A', 'B', 'C']
    player_moves = ['X', 'Y', 'Z']
    lines = input.read().splitlines()
    games = [line.split() for line in lines]
    # print(games)
    for game in games:
        oMove = opponent_moves.index(game[0])
        pMove = player_moves.index(game[1])

        # 0 -> rock
        # 1 -> paper
        # 2 -> scissors

        # draw
        if oMove == pMove:
            player_score += pMove + 4 # move + draw + 1 for 1-index
            continue 

        # win
        if (pMove == 0 and oMove == 2) or (pMove == 1 and oMove == 0) or (pMove == 2 and oMove == 1):
            player_score += pMove + 7
            continue

        # loss
        if (pMove == 0 and oMove == 1) or (pMove == 1 and oMove == 2) or (pMove == 2 and oMove == 0):
            player_score += pMove + 1
            continue

    print(player_score)