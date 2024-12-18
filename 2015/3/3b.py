import sys

with open(sys.argv[1]) as f:
    text = f.read()
    santa = set()
    robo = set()

    santa.add((0, 0,))

    sx, sy = 0, 0
    rx, ry = 0, 0

    i = 0
    for move in text:
        if i % 2 == 0:
            if move == 'v':
                sy += 1
            if move == '>':
                sx += 1
            if move == '^':
                sy -= 1
            if move == '<':
                sx -= 1
            santa.add((sx, sy,))
        else:
            if move == 'v':
                ry += 1
            if move == '>':
                rx += 1
            if move == '^':
                ry -= 1
            if move == '<':
                rx -= 1
            robo.add((rx, ry,))
        i += 1

    print(len(santa.union(robo)))

