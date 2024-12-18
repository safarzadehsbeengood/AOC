with open('input.txt', 'r') as input:
    grid = [[*line] for line in input.read().splitlines()]
    m, n = len(grid), len(grid[0])
    # for row in grid:
    #     print(''.join(row))
    points = dict()
    for i in range(1, m):
        for j in range(n):
            if grid[i][j] == 'O':
                y = i
                while y > 0 and grid[y-1][j] != '#' and grid[y-1][j] != 'O':
                    # swap 
                    grid[y-1][j] = 'O'
                    grid[y][j] = '.'
                    y -= 1
    # print()
    sum = 0
    for level, row in enumerate(grid):
        sum += row.count('O') * (n - level)
        # print(''.join(row))
    print(sum)

    # for point, dist in points.items():
    #     print(point, dist)
    # print(sum(points.values()))
