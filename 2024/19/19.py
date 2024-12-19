import sys
from functools import cache

with open(sys.argv[1]) as f:
    towels, patterns = f.read().split('\n\n')
    towels = towels.split(', ')
    patterns = patterns.splitlines()

    ct = 0

    memo = {}

    def find(pattern):
        if len(pattern) == 0:
            return True
        if memo.get(pattern) != None:
            return memo[pattern]
        else:
            for towel in towels:
                if pattern.startswith(towel):
                    res = find(pattern[len(towel):])
                    memo[pattern] = res
                    if res:
                        return True
            return False

    for pattern in patterns:
        if find(pattern):
            ct += 1
    print(ct)

    # pt 2

    @cache
    def find2(pattern):
        if len(pattern) == 0:
            return 1
        ways = 0
        for towel in towels:
            if pattern.startswith(towel):
                ways += find2(pattern[len(towel):])
        return ways

    pt2 = 0
    for pattern in patterns:
        pt2 += find2(pattern)
    print(pt2)

