import re
pattern = re.compile(r"-?\d+")
Y = 2000000
# Y = 10
known = set()
cannot = set()
intervals = []

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

with open('input.txt', 'r') as input:
    for line in input.read().splitlines():
        # grab the sensor and beacon coords
        sx, sy, bx, by = map(int, pattern.findall(line))

        d = dist(sx, sy, bx, by) # calc distance between beacon and sensor
        o = d - abs(sy - Y) # get the offset of the x interval at Y

        # if the offset is negative, Y is out of range so this sensor won't help
        if o < 0:
            continue

        # get the interval
        lx = sx - o 
        hx = sx + o

        # go through the interval and gather the x coords where beacons cannot be
        for x in range(lx, hx+1):
            cannot.add(x)

        # if the beacon is on Y, add it to the known points
        if by == Y:
            known.add(bx)

# the set difference is the number of x-coords on Y where beacons cannot be
print(len(cannot - known))