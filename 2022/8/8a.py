from tqdm import tqdm
visible = 0
with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    grid = [list(map(int, line)) for line in lines]
    rows, columns = len(grid), len(grid[0])
    print(f'{rows} x {columns}')
    
    for i in tqdm(range(rows)):
        for j in range(columns):
            # if on an edge, it's visible
            if j == 0 or i == 0 or j == columns-1 or i == rows-1:
                visible += 1
                continue
            # left and right
            if (max(grid[i][:j]) < grid[i][j]) or (max(grid[i][j+1:]) < grid[i][j]):
                visible += 1
                continue
            # above and below
            if (max(list(grid[a][j] for a in range(i-1, -1, -1))) < grid[i][j]) or (max(list(grid[b][j] for b in range(i+1, rows))) < grid[i][j]):
                visible += 1
                continue

    print(visible)