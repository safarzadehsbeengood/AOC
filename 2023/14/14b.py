from tqdm import tqdm
def rollNorth(grid, m, n):
    for i in range(1, m):
            for j in range(n):
                if grid[i][j] == 'O':
                    y = i
                    while y > 0 and grid[y-1][j] != '#' and grid[y-1][j] != 'O':
                        # swap 
                        grid[y-1][j] = 'O'
                        grid[y][j] = '.'
                        y -= 1

def rollSouth(grid, m, n):
    for i in range(m-1, -1, -1):
            for j in range(n):
                if grid[i][j] == 'O':
                    y = i
                    while y < m-1 and grid[y+1][j] != '#' and grid[y+1][j] != 'O':
                        # swap 
                        grid[y+1][j] = 'O'
                        grid[y][j] = '.'
                        y += 1

def rollEast(grid, m, n):
     for j in range(n-1, -1, -1):
          for i in range(m):
               if grid[i][j] == 'O':
                    x = j
                    while x < n-1 and grid[i][x+1] != '#' and grid[i][x+1] != 'O':
                         grid[i][x+1] = 'O'
                         grid[i][x] = '.'
                         x += 1

def rollWest(grid, m, n):
     for j in range(n):
          for i in range(m):
               if grid[i][j] == 'O':
                    x = j
                    while x > 0 and grid[i][x-1] != '#' and grid[i][x-1] != 'O':
                         grid[i][x-1] = 'O'
                         grid[i][x] = '.'
                         x -= 1

with open('input.txt', 'r') as input:
    grid = [[*line] for line in input.read().splitlines()]
    m, n = len(grid), len(grid[0])
    first_cfg = '\n'.join([''.join(line) for line in grid])
    seen = set(first_cfg)
    grids = [first_cfg]
    iter = 0
    for _ in tqdm(range(100000)):
        iter += 1
        rollNorth(grid, m, n)
        rollWest(grid, m, n)
        rollSouth(grid, m, n)
        rollEast(grid, m, n)
        cfg = '\n'.join([''.join(line) for line in grid])
        if cfg in seen:
            break
        seen.add(cfg)
        grids.append(cfg)
    first = grids.index(cfg)
    x = (1000000000 - first) % (iter-first) + first
    sum = 0
    for level, row in enumerate(grids[x].splitlines()):
        sum += row.count('O') * (m - level)
    print(sum)
