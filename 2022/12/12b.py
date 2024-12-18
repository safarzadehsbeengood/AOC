from collections import deque
with open('input.txt', 'r') as input:
    grid = [list(x) for x in input.read().strip().splitlines()]
    # for l in grid: print(''.join(l))

    # replace 'S' and 'E' with 'a' and 'z' for convenience
    for r, row in enumerate(grid):
        for c, item in enumerate(row):
            if item == 'S':
                grid[r][c] = 'a'
            if item == 'E':
                er = r 
                ec = c 
                grid[r][c] = 'z'

    q = deque()
    q.append((0, er, ec)) # start at the end point

    # visited set
    vis = {(er, ec)}
    
    while q:
        # pop a node
        d, r, c = q.popleft()

        # look at neighbors
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            # if out of bounds, continue
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue 
            # if already visited, continue
            if (nr, nc) in vis:
                continue 
            # if we can't step to it, continue
            if ord(grid[nr][nc]) - ord(grid[r][c]) < -1:
                continue 
            # if we've found a starting point, print the distance it took
            if grid[nr][nc] == 'a':
                print(d+1)
                exit(0)
            # otherwise, add this node to the visited set
            vis.add((nr, nc))
            # and add this neighbor to the queue
            q.append((d+1, nr, nc))
