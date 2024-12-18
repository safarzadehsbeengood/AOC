def findReflection(grid):
    for i in range(1, len(grid)):
            above = grid[:i][::-1]
            below = grid[i:]
            above = above[:len(below)]
            below = below[:len(above)]
            if above == below: return i
    return 0
with open('input.txt', 'r') as input:
    patterns = [pattern.splitlines() for pattern in input.read().split('\n\n')]
    total = 0
    for pattern in patterns:
         row = findReflection(pattern)
         total += row * 100
         col = findReflection(list(zip(*pattern)))
         total += col
    print(total)