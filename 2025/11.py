from aocd import get_data
from functools import cache

data_source = get_data(day=11, year=2025)

paths = []

def build_graph(data):
    g = {}
    for line in data.splitlines():
        v, n = line.split(":")
        n = n.strip().split()
        g[v] = set(n)
    return g

g = build_graph(data_source)

def dfs(src, target, path, g):
    new_path = path + [src]
    if src == target:
        paths.append(new_path)
    else:
        for adj in g.get(src, []):
            dfs(adj, target, new_path, g)
    if path:
        path.pop()

@cache
def dfs2(src, dac, fft):
    if src == 'out': return dac and fft
    return sum(dfs2(dst, dac or dst=='dac', fft or dst=='fft') for dst in g[src])
        

dfs("you", "out", [], g)
print(len(paths))
print(dfs2("svr", False, False))
