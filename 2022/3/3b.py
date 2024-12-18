def prioritize(c):
    score = ord(c.lower()) + 26 - 96 if c.isupper() else ord(c.lower()) - 96
    return score

with open('input.txt', 'r') as input:
    common = []
    lines = input.read().splitlines()
    # print(len(lines))
    for i in range(0, len(lines), 3):
        # print(line)
        mid = int(len(lines[i]) / 2)
        r1 = lines[i]
        r2 = lines[i+1]
        r3 = lines[i+2]
        for c in r1: 
            if c in r2 and c in r3:
                # print(f'{r1}\n{r2} -> {c}: {prioritize(c)}\n{r3}\n\n')
                common.append(prioritize(c))
                break
    # print(common)
    print(sum(common))