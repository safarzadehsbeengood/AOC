import time
import math
from itertools import cycle
with open('input.txt', 'r') as input:
    # preprocess
    nodes = {}
    lines = input.read().splitlines()
    instruction = lines[0]
    for node in lines[2:]:
        info = node.split(' = ')
        n = info[0]
        p = info[1].split(', ')
        a, b = p[0][1:], p[1][:-1]
        nodes[n] = (a, b)
    # for node, p in nodes.items():
    #     print(f'{node}: {p}')
    loops = []
    starting = [node for node in list(nodes.keys()) if node[-1] == 'A']
    for node in starting:
        cycler = cycle(instruction)
        steps = 0
        while not node.endswith('Z'):
            instruction = next(cycler)
            left, right = nodes[node]
            node = left if instruction == 'L' else right
            steps += 1
            if steps == 1000000:
                assert False, 'infinite loop'
        loops.append(steps)
    print(math.lcm(*loops))
