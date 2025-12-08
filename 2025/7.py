from aocd import get_data
from functools import cache

data_source = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

data_source = get_data(day=7, year=2025)

data = [[*line] for line in data_source.splitlines()]

# pt 1
grid = data.copy()

sj = grid[0].index("S") # starting col
i = 1
# first beam
res = 1
while grid[i][sj] != "^":
    grid[i][sj] = "|"
    i += 1
si = i # starting row
i += 1

beam_indices = set([sj-1, sj+1])
while i < len(grid)-1:
    to_split = []
    for j in beam_indices:
        if grid[i][j] == "^":
            to_split.append(j)
            res += 1
    for j in to_split:
        beam_indices.remove(j)
        if 0 <= j-1:
            beam_indices.add(j-1)
        if j+1 < len(grid[j]):
            beam_indices.add(j+1)        
    i += 1
print(res)

# pt 2

def valid(i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

# use recursion

@cache # for memoization
def laser(i, j):
    # leaf, return 1 way
    if i == len(grid):
        return 1
    # not valid, can't continue
    if not valid(i, j):
        return 0 
    
    if grid[i][j] == "^":
        return laser(i+1, j+1) + laser(i+1, j-1)
    return laser(i+1, j)

print(laser(si, sj))