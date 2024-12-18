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

    for s, o in zip(seeds[::2], seeds[1::2]):
        ranges = [(s, s + o - 1)]
        for typemappings in mappings:
            newranges = []
            for l, h in ranges:
                found = False
                for md, ms, mo in typemappings:
                    print(f'l: {l} h: {h} md: {md} ms: {ms} mo: {mo}')
                    if l >= ms and h < ms + mo:
                        newranges.append((l - ms + md, h - ms + md))
                        found = True
                    elif l < ms and h >= ms and h < ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + h - ms))
                        found = True
                    elif l < ms + mo and h >= ms + mo and l >= ms:
                        ranges.append((ms + mo, h))
                        newranges.append((md + l - ms, md + mo - 1))
                        found = True
                    elif l < ms and h >= ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + mo - 1))
                        ranges.append((ms + mo, h))
                        found = True
                    if found == True:
                        break
                if found == False:
                    newranges.append((l, h))
            ranges = newranges.copy()
        res = min(res, min(ranges)[0])
    print(res)