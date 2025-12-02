import sys

f = open(sys.argv[1])

schematics = f.read().split('\n\n')

keys = []
locks = []

def convert_to_heights(schematic):
    heights = []
    grid = [[*line] for line in schematic.splitlines()]
    for c in range(len(grid[0])):
        height = 0
        for r in range(len(grid)):
            height += grid[r][c] == '#'
        heights.append(height-1)
    return tuple(heights)

def eval(key, lock):
    valid = all([a+b<=5 for a, b in zip(key, lock)])
    return valid
    

for schematic in schematics:
    if schematic.startswith('#####'):
        locks.append(convert_to_heights(schematic))
    else:
        keys.append(convert_to_heights(schematic))

res = 0

for lock in locks:
    for key in keys:
        if eval(key, lock):
            res += 1

print(res)

