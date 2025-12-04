from aocd import get_data

directions = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]

# test = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

# grid = test.splitlines()

grid = get_data(day=4, year=2025).splitlines()

# pt 1
res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != '@': continue
        ct = 0
        for (di, dj) in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni <= len(grid)-1 and 0 <= nj <= len(grid[0])-1 and grid[ni][nj] == '@':
                ct += 1 
        if ct < 4:
            res += 1

print(res)

def remove_rolls(g):
    res = 0
    new_grid = []
    for i in range(len(grid)):
        row = ''
        for j in range(len(grid[0])):
            if grid[i][j] != '@': 
                row += grid[i][j]
                continue
            ct = 0
            for (di, dj) in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni <= len(grid)-1 and 0 <= nj <= len(grid[0])-1 and grid[ni][nj] == '@':
                    ct += 1 
            if ct < 4:
                row += 'x'
                res += 1
            else:
                row += "@"
        new_grid.append(row)
                
    return res, new_grid

removed = res
res = 0

while removed > 0:
    removed, grid = remove_rolls(grid)
    res += removed
    
print(res)


