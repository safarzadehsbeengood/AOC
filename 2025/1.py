from aocd import get_data

rotations = get_data(day=1, year=2025).splitlines()
# rotations = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".splitlines()

d = 50
res = 0

directions = {
    "L": -1,
    "R": 1
}

for rotation in rotations:
    # get direction and distance
    direction, distance = directions[rotation[0]], int(rotation[1:])
    
    # account for full rotations
    full_rotations = distance // 100
    res += full_rotations
    distance -= full_rotations * 100
    
    # print(f"{rotation} {d} -> {(d + direction*distance)%100}", end=" ")
    # twist dial 
    old_d = d
    d += direction*distance
    
    # check if dial passed or is 0
    if d <= 0 or d >= 100:
        d %= 100
        if old_d != 0:
            res += 1
    
print(res)


    