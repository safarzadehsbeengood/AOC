with open('input.txt', 'r') as input:
    LOSE = 0
    DRAW = 1
    WIN = 2
    player_score = 0
    won = False
    opponent_moves = ['A', 'B', 'C']
    player_moves = ['X', 'Y', 'Z']
    lines = input.read().splitlines()
    games = [line.split() for line in lines]
    # print(games)
    for game in games:
        oMove = opponent_moves.index(game[0])
        status = player_moves.index(game[1])

        # 0 -> rock
        # 1 -> paper
        # 2 -> scissors

        # draw
        if status == DRAW:
            player_score += 4 + oMove

        # win
        if status == WIN:
            if oMove == 0:
                player_score += 8
            elif oMove == 1:
                player_score += 9
            elif oMove == 2:
                player_score += 7
            continue

        # loss
        if status == LOSE:
            if oMove == 0:
                player_score += 3
            elif oMove == 1:
                player_score += 1
            elif oMove == 2:
                player_score += 2
            continue

    print(player_score)