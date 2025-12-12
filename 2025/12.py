from aocd import get_data

data_source = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

data_source = get_data(day=12, year=2025)

blocks = data_source.split("\n\n")
shps, regions = blocks[:-1], blocks[-1]

shapes = {}
for s in shps:
    x = s.split(":")
    ct = x[1].strip().count("#")
    shapes[int(x[0])] = ct
    
pt1 = 0
for region in regions.splitlines():
    size, shape_indices = region.split(":")
    shape_indices = list(map(int, shape_indices.split()))
    size = eval(size.replace("x", "*"))
    required = sum([shapes[i]*ct for i, ct in enumerate(shape_indices)])
    if required <= size:
        pt1 += 1

print(pt1)


    

    