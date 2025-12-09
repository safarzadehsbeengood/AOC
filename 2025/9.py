from aocd import get_data
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

data_source = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

data_source = get_data(day=9, year=2025)

points = [list(map(int, line.split(","))) for line in data_source.splitlines()]

# pt 1
def area(r1, c1, r2, c2):
    return (abs(r2-r1)+1) * (abs(c2-c1)+1)

areas = {}
for i in range(len(points)):
    for j in range(i+1, len(points)):
        r1, c1 = points[i]
        r2, c2 = points[j]
        areas[(i, j,)] = area(r1, c1, r2, c2)

print(max(areas.values()))

# pt 2
# create a polygon
polygon = Polygon(points)

x,y = polygon.exterior.xy
plt.plot(x,y)

max_rect = None
max_area = float("-inf")
valid_areas = []
for (i, j), area in areas.items():
    p1, p2 = points[i], points[j]
    rect = Polygon([p1, (p2[0], p1[1]), p2, (p1[0], p2[1])])
    if polygon.contains(rect):
        max_area = max(max_area, area)
        max_rect = rect

print(max_area)
x, y = max_rect.exterior.xy
plt.plot(x, y)
plt.show()
