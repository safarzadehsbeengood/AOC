import sys
from itertools import product
from functools import cache

# dicts to store path from one key to another
npm = {}
dpm = {}

numpad = [[*line] for line in '789\n456\n123\n 0A'.splitlines()]
dpad = [[*line] for line in ' ^A\n<v>'.splitlines()]

# input map
im = {
    (1, 0): 'v',
    (-1, 0): '^',
    (0, 1): '>',
    (0, -1): '<'
}
dirs = list(im.keys()) # directions

# manhattan distance
def dist(pos, end):
    pi, pj = pos
    ei, ej = end
    return abs(pi-ei) + abs(pj-ej)

# returns all paths from start pos of numpad to end pos of numpad
def gdfs_np(start, end):
    seen = set()
    seen.add(start)
    p = ''
    paths = []
    def gdfs_nph(pos, end, path):
        i, j = pos 
        # print(pos, end, path)
        if pos == end: paths.append(path+'A')
        neighbors = sorted([(i+di, j+dj,) for di, dj in dirs if 0<=i+di<len(numpad) and 0<=j+dj<len(numpad[0]) and (i+di, j+dj,) not in seen and numpad[i+di][j+dj] != ' '], key=lambda x: dist(x, end))
        for neighbor in neighbors:
            seen.add(neighbor)
            gdfs_nph(neighbor, end, path+im[(neighbor[0]-i, neighbor[1]-j)])
            seen.remove(neighbor)
    gdfs_nph(start, end, p)
    optimal_len = len(sorted(paths, key=lambda x: len(x))[0])
    paths = [path for path in paths if len(path) == optimal_len]
    return paths

# returns all shortest paths from start pos of dpad to end pos of dpad
def gdfs_dp(start, end):
    seen = set()
    seen.add(start)
    p = ''
    paths = []
    def gdfs_dph(pos, end, path):
        i, j = pos 
        # print(pos, end, path)
        if pos == end: paths.append(path+'A')
        neighbors = sorted([(i+di, j+dj,) for di, dj in dirs if 0<=i+di<len(dpad) and 0<=j+dj<len(dpad[0]) and (i+di, j+dj,) not in seen and dpad[i+di][j+dj] != ' '], key=lambda x: dist(x, end))
        for neighbor in neighbors:
            seen.add(pos)
            gdfs_dph(neighbor, end, path+im[(neighbor[0]-i, neighbor[1]-j)])
            seen.remove(pos)
    gdfs_dph(start, end, p)
    optimal_len = len(sorted(paths, key=lambda x: len(x))[0])
    paths = [path for path in paths if len(path) == optimal_len]
    return paths


# build map of paths from one numpad key to another
for i in range(len(numpad)):
    for j in range(len(numpad[0])):
        if numpad[i][j] == ' ': continue
        for k in range(len(numpad)):
            for l in range(len(numpad[0])):
                if numpad[k][l] == ' ': continue
                npm[(numpad[i][j], numpad[k][l])] = gdfs_np((i, j,), (k,l,))

# build map of paths from one dpad key to another
for i in range(len(dpad)):
    for j in range(len(dpad[0])):
        if dpad[i][j] == ' ': continue
        for k in range(len(dpad)):
            for l in range(len(dpad[0])):
                if dpad[k][l] == ' ': continue
                dpm[(dpad[i][j], dpad[k][l],)] = gdfs_dp((i,j,), (k,l,))

dlm = {k: len(v[0]) for k, v in dpm.items()}

@cache
def cl(x, y, depth=2):
    if depth == 1:
        return dlm[(x, y)]
    optimal = float("inf")
    for s in dpm[(x, y)]:
        l = 0
        for nx, ny in zip("A" + s, s):
            l += cl(nx, ny, depth-1)
        optimal = min(optimal, l)
    return optimal


with open(sys.argv[1]) as f:
    codes = f.read().splitlines()
    pt2 = 0
    for code in codes:
        m = float("inf")
        r1 = [npm[(f, t)] for f, t in zip("A" + code, code)]
        r1 = [''.join(prod) for prod in product(*r1)]
        for s in r1:
            l = 0
            for x, y in zip("A" + s, s):
                l += cl(x, y, 25)
            m = min(m, l)
        pt2 += m * int(code[:-1])
    print(pt2)

        
        
                




