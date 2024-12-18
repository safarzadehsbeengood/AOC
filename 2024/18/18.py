import sys
from collections import deque

with open(sys.argv[1]) as f:
    s = 70
    coords = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]
    def check(n):
        grid = [["."]*(s+1) for _ in range(s+1)]

        for j, i in coords[:n]:
            grid[i][j] = '#'
        
        # bfs 
        queue = deque([(0, 0)])
        seen = {(0, 0)}

        while queue:
            r, c = queue.popleft()
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if nr < 0 or nr > s or nc < 0 or nc > s or grid[nr][nc] == '#' or (nr, nc) in seen:
                    continue
                if nr == nc == s: return True
                queue.append((nr, nc))
                seen.add((nr, nc))
        return False
    
    for n in range(1, len(coords)):
        if check(n) == False:
            print(coords[n-1])
            break