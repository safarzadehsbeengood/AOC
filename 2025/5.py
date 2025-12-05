from aocd import get_data
from tqdm import tqdm

data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

data = get_data(day=5, year=2025)

ranges, ids = data.split("\n\n")

ranges = [list(map(int, line.split('-'))) for line in ranges.splitlines()]
ids = list(map(int, ids.splitlines()))

print(ranges, ids)

# pt 1
res = 0

for id in ids:
    found = False
    for start, end in ranges:
        if id in range(start, end+1): 
            # print(id, start, "-", end)
            res += 1
            found = True
            break
    if found: continue
    
print(res)

# pt 2
res = 0

def is_overlapping(x: tuple[int, int], y: tuple[int, int]):
    return x[0] <= y[1] and y[0] <= x[1]

ranges.sort(key=lambda x: x[0])

merged = [ranges[0]]
for interval in ranges[1:]:
    if is_overlapping(merged[-1], interval):
        merged[-1][-1] = max(interval[1], merged[-1][-1])
    else:
        merged.append(interval)

print(sum([end-start+1 for start, end in merged]))
        