import sys

with open(sys.argv[1]) as f:
    text = f.read()
    print(text.count('(')-text.count(')'))
    floor = 0
    i = 0
    for c in text:
        if floor < 0:
            print(i)
            break
        if c == '\n': continue
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        i += 1

