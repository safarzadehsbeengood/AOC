import sys

with open(sys.argv[1]) as f:
    text = f.read().splitlines()
    paper = 0
    ribbon = 0

    for line in text:
        l, w, h = list(map(int, line.split('x')))
        x, y, z = l*w, w*h, l*h
        print(l, w, h)
        paper += 2*x+2*y+2*z+min(x, y, z)
        dims = sorted((l, w, h))
        ribbon += l*w*h + (dims[0]*2+dims[1]*2)
    print(paper)
    print(ribbon)

