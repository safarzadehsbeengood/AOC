import sys

f = open(sys.argv[1])
pairs = [line.split('-') for line in f.read().splitlines()]

conns = {}

for a, b in pairs:
    if a not in conns: conns[a] = set()
    if b not in conns: conns[b] = set()
    conns[a].add(b)
    conns[b].add(a)

all_sets = set()

def find(host, seen):
    prereq = tuple(sorted(seen))
    if prereq in all_sets: return
    all_sets.add(prereq)
    for neighbor in conns[host]:
        if neighbor in seen: continue
        if not seen <= conns[neighbor]: continue
        find(neighbor, seen | {neighbor})
       
for host in conns:
    find(host, {host})


maxlen = max(map(len, all_sets))
print(','.join(list([s for s in all_sets if len(s) == maxlen][0])))
