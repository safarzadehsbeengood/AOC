from tqdm import tqdm
scores = []
with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    grid = [list(map(int, line)) for line in lines]
    rows, columns = len(grid), len(grid[0])
    # for row in grid:
    #     print(' '.join(list(map(str, row))))
    
    print(f'\n{rows} x {columns}\n')
    
    for i in range(rows):
        row_score = []
        for j in range(columns):
            curr = grid[i][j]
            up = left = down = right = 0
            
            # visible trees to the left
            if j > 0:
                for x in range(j-1, -1, -1):
                    left += 1
                    if grid[i][x] >= curr:
                        break

            # right
            if j < columns-1:
                for x in range(j+1, columns):
                    right += 1
                    if grid[i][x] >= curr:
                        break

            # up
            if i > 0:
                for y in range(i-1, -1, -1):
                    up += 1
                    if grid[y][j] >= curr:
                        break
            
            # down
            if i < rows-1:
                for y in range(i+1, rows):
                    down += 1
                    if grid[y][j] >= curr:
                        break
            score = up * down * left * right
            # row_score.append(score)
            scores.append(score)
        # print(' '.join(list(map(str, row_score))))

print(max(scores))
