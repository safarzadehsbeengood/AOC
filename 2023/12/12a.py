with open('input.txt') as input:
    def count(cfg, groups):
        if cfg == '':
            return 1 if groups == () else 0
        if groups == ():
            return 0 if "#" in cfg else 1
        result = 0
        if cfg[0] in ".?":
            result += count(cfg[1:], groups)
        if cfg[0] in "#?":
            if groups[0] <= len(cfg) and '.' not in cfg[:groups[0]] and (groups[0] == len(cfg) or cfg[groups[0]] != '#'):
                result += count(cfg[groups[0]+1:], groups[1:])
        return result
    total = 0
    for line in input.read().splitlines():
        cfg, groups = line.split()
        groups = tuple(map(int, groups.split(',')))
        total += count(cfg, groups)
    print(total)