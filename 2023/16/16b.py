from collections import deque

with open('input.txt', 'r') as input:
    grid = input.read().splitlines()
    def calc(r, c, dr, dc):
        start = [(r, c, dr, dc)]
        seen = set()
        queue = deque(start)
        while queue:
            r, c, dr, dc = queue.popleft()

            r += dr 
            c += dc

            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                continue

            ch = grid[r][c]
            if ch == '.' or (ch == '|' and dr != 0) or (ch == '-' and dc != 0):
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    queue.append((r, c, dr, dc))
            elif ch == '/':
                dr, dc = -dc, -dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    queue.append((r, c, dr, dc))
            elif ch == '\\':
                dr, dc = dc, dr
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    queue.append((r, c, dr, dc))
            else:
                for dr, dc in [(1, 0), (-1, 0)] if ch == '|' else [(0, -1), (0, 1)]:
                    if (r, c, dr, dc) not in seen:
                        seen.add((r, c, dr, dc))
                        queue.append((r, c, dr, dc))
        

        coords = {(r, c) for (r, c, _, _) in seen}
        return len(coords)
    
    maxval = 0
    for r in range(len(grid)):
        maxval = max(maxval, calc(r, -1, 0, 1))
        maxval = max(maxval, calc(r, len(grid[0]), 0, -1))
    for c in range(len(grid[0])):
        maxval = max(maxval, calc(-1, c, 1, 0))
        maxval = max(maxval, calc(len(grid), c, -1, 0))
    print(maxval)