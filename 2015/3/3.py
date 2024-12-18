import sys

with open(sys.argv[1]) as f:
    text = f.read()
    seen = set()
    x, y = 0, 0
    seen.add((x, y,))

    for move in text:
        if move == 'v':
            y += 1
        if move == '>':
            x += 1
        if move == '^':
            y -= 1
        if move == '<':
            x -= 1
        seen.add((x, y,))

    print(len(seen))



