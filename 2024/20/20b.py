import sys
from collections import deque

with open(sys.argv[1]) as f:
    grid = [[*line] for line in f.read().splitlines()]
    m, n = len(grid), len(grid[0])

    # find start and end
    start = tuple()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j,)

    def bfs(g):
        q = deque()
        seen = set()
        prev = {}

        def add(i, j, dist, pi, pj):
            if (i, j) in seen:
                return
            if pi != None:
                prev[(i, j,)] = (pi, pj)
            seen.add((i, j,))
            q.append((i, j, dist,))

        add(start[0], start[1], 0, None, None)

        while q:
            curr = q[0]
            i, j, dist = curr
            if g[i][j] == 'E':
                path = [(i, j,)]
                while path[-1] in prev:
                    path.append(prev[path[-1]])
                return path
            q.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if g[ni][nj] in '.E':
                    add(ni, nj, dist+1, i, j)
        return []

    o = bfs(grid)
    # print(o)
    pt2 = 0
    for i in range(len(o)):
        for j in range(i+1, len(o)):
            d = abs(o[i][0] - o[j][0]) + abs(o[i][1] - o[j][1])
            # print(d)
            if d > 20:
                continue
            np = i + d + len(o) - j - 1
            if np <= len(o)-1-100:
                pt2 += 1
    print(pt2)

