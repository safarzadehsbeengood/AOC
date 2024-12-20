import sys
from collections import deque
from tqdm import tqdm

with open(sys.argv[1]) as f:
    grid = [[*line] for line in f.read().splitlines()]
    m, n = len(grid), len(grid[0])

    # find start and end
    start, end = tuple(), tuple()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j, 0,)
            # elif grid[i][j] == 'E':
                # end = (i, j, 0)

    removable = []
    for i in range(1, m-1):
        for j in range(1, n-1):
            if grid[i][j] == '#' and ((grid[i][j+1] in '.ES' and grid[i][j-1] in '.ES') or (grid[i+1][j] in '.ES' and grid[i-1][j] in '.ES')):
                removable.append((i, j,))
    # print(removable)

    def bfs(g):
        q = deque()
        seen = set()
        si, sj, _ = start
        q.append(start)
        seen.add((si, sj,))
        while q:
            curr = q.popleft()
            i, j, ps = curr
            if g[i][j] == 'E':
                return ps
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if (ni, nj,) in seen: continue
                if g[ni][nj] == '#': continue
                q.append((ni, nj, ps+1))
                seen.add((ni, nj,))
        return float("inf")

    original = bfs(grid)
    pt1 = 0
    with tqdm(total=len(removable)) as pbar:
        for coord in removable:
            ri, rj = coord
            grid[ri][rj] = '.'
            res = bfs(grid)
            grid[ri][rj] = '#'
            if original-res >= 100:
                # print(res-original)
                pt1 += 1
            pbar.update()

    print(pt1)
