from collections import deque
from time import sleep
import os
from colorama import init, Fore
init(autoreset=True)

pipes = {
    '|': ['n', 's'],
    '-': ['w', 'e'],
    'L': ['n', 'e'],
    'J': ['n', 'w'],
    '7': ['s', 'w'],
    'F': ['s', 'e'],
    'S': ['n', 'w', 's', 'e']
}

directions = {
    'n': (-1, 0, 's'),
    's': (1, 0, 'n'),
    'e': (0, 1, 'w'),
    'w': (0, -1, 'e')
}

def printGrid(pos, grid):
    y, x = pos
    os.system('clear')
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                if j == n-1:
                    print(Fore.RED + grid[i][j])
                elif i == y and j == x:
                    if j == n-1:
                        print(Fore.GREEN + grid[i][j])
                    else:
                        print(Fore.GREEN + grid[i][j], end='')

                else:
                    print(Fore.RED + grid[i][j], end='')
            else:
                if j == n-1:
                    print(grid[i][j])
                else:
                    print(grid[i][j], end='')


with open('test_input.txt', 'r') as input:
    grid = [[*line] for line in input.read().splitlines()]
    for i in range(len(grid)):
        # print(''.join(grid[i]))
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
                print(f'start: {start}')
    m = len(grid)
    n = len(grid[0])

    visited = dict() # visited spots + distance

    searching = deque()
    searching.append((start, 0))

    while searching:
        curr, dist = searching.popleft()
        printGrid(curr, grid)
        # sleep(0.1)
        if visited.get(curr):
            continue
        visited[curr] = dist
        y, x = curr
        can_go = pipes[grid[y][x]]
        print(can_go)
        for direction in can_go:
            dy, dx, opposite = directions[direction]
            new = (y+dy, x+dx)
            if new[0] < 0 or new[0] >= len(grid):
                continue
            if new[1] < 0 or new[1] >= len(grid[0]):
                continue 
            target = grid[new[0]][new[1]]
            if target not in pipes:
                continue 
            target_directions = pipes[target]
            if opposite in target_directions:
                searching.append((new, dist+1))
    maximum = max(visited.values())
    max_point = None
    for point, distance in visited.items():
        # grid[point[0]][point[1]] = str(distance)
        if distance == maximum:
            max_point = point

    print(max(visited.values()))
    # printGrid(max_point, grid)

