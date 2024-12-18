def prioritize(c):
    score = ord(c.lower()) + 26 - 96 if c.isupper() else ord(c.lower()) - 96
    return score

with open('input.txt', 'r') as input:
    common = []
    lines = input.read().splitlines()
    # print(lines)
    for line in lines:
        # print(line)
        mid = int(len(line) / 2)
        r1 = line[:mid]
        r2 = line[mid:]
        for c in r1: 
            if c in r2:
                # print(f'{"".join(sorted(r1))} -> {c}: {prioritize(c)}\n{"".join(sorted(r2))}\n ' + '^'.rjust("".join(sorted(r2)).find(c)))
                common.append(prioritize(c))
                break
    # print(common)
    print(sum(common))