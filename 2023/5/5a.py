seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humidity = []
humidity_to_location = []

def seed_to_location(seed):
    # to soil
    for interval in seed_to_soil:
        pass

with open('input.txt', 'r') as input:
    # preprocess
    lines = input.readlines()
    seeds = [int(seed) for seed in lines[0].split(': ')[1].split()]
    mappings = []
    for line in lines[2:]:
        line = line.strip()
        if line.endswith(':'):
            mappings.append([])
        elif len(line) > 0:
            mappings[-1].append([int(i) for i in line.split(' ')])
    
    [m.sort(key = lambda x: x[1]) for m in mappings]

    res = 2**32

    for x in seeds:
        for typemappings in mappings:
            for mapping in typemappings:
                if (x >= mapping[1]) and (x < mapping[1] + mapping[2]):
                    x = x - mapping[1] + mapping[0]
                    break
        res = min(x, res)
    print(res)