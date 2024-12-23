import sys
from itertools import product

f = open(sys.argv[1])
pairs = [line.split('-') for line in f.read().splitlines()]

conns = {}

for a, b in pairs:
    if a not in conns: conns[a] = set()
    if b not in conns: conns[b] = set()
    conns[a].add(b)
    conns[b].add(a)

seen = set()
res = 0
for host, connections in conns.items():
    for connection in connections:
        for third_conn in conns[connection]:
            if third_conn != host and host in conns[third_conn]:
                seen.add(tuple(sorted([host, connection, third_conn])))

for grp in seen:
    if any([host.startswith('t') for host in grp]):
        res += 1

print(res)
