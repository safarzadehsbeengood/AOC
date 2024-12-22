import sys
import curses
from time import sleep

with open(sys.argv[1]) as f:
    text = f.read()

grid, moves = text.split('\n\n')

grid = [[*line] for line in grid.splitlines()]

m = len(grid)
n = len(grid[0])

moves = moves.replace('\n', '')

# find start
start = tuple() 
for i in range(m):
    for j in range(n):
        if grid[i][j] == '@':
            start = (i, j)
        if grid[i][j] == '.':
            grid[i][j] = ' '

dirs = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0)
}

i, j = start
moves = moves.strip()

def move(dir):
    global i, j, grid
    di, dj = dirs[dir]
    # if a wall in front, continue
    if grid[i+di][j+dj] == '#':
        return
    # if an empty space in front, move there
    if grid[i+di][j+dj] == ' ':
        grid[i+di][j+dj], grid[i][j] = grid[i][j], grid[i+di][j+dj]
        i += di
        j += dj
        return
    else:
        # find the last box in the chain of boxes in front of the robot
        bi, bj = i+di, j+dj
        while grid[bi][bj] == 'O':
            bi += di
            bj += dj
        # if the last box has a wall in front of it, we can't push the box(es)
        if grid[bi][bj] == '#':
            return
        # otherwise, we can just swap the box in front of the robot with the empty spot
        # in front of the robot 
        else:
            grid[i+di][j+dj], grid[bi][bj] = grid[bi][bj], grid[i+di][j+dj]

        grid[i+di][j+dj], grid[i][j] = grid[i][j], grid[i+di][j+dj]
        i += di
        j += dj


COLOR_MAP = {
    "O": 7,
    "@": 10,
    "#": 254,
    ' ': 10
}

def main(stdscr: curses.window):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for i in range(curses.COLORS-1):
        curses.init_pair(i, i, -1)

    curses.init_pair(7, 7, 7)
    curses.init_pair(254, 254, 254)
    stdscr.clear()
    def curses_printgrid():
        stdscr.clear()
        x, y = 0, 0
        for row in grid:
            for c in row:
                # stdscr.addch(y, x, c, curses.color_pair(COLOR_MAP[c]))
                stdscr.addch(y, 20+x, c)
                x += 1
            x = 0
            y += 1

    for mov in moves:
        curses_printgrid()
        move(mov)
        stdscr.refresh()
        # sleep(0.1)

    sleep(10)

curses.wrapper(main)

