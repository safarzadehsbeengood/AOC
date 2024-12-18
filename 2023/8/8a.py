import time
with open('input.txt', 'r') as input:
    nodes = {}
    steps = 0
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
    curr = 'AAA'
    while (curr != 'ZZZ'):
        for x in instruction:
            # print(f'{curr}: ({" ".join(nodes[curr])}) -> {x}')
            # time.sleep(1)
            if curr == 'ZZZ':
                print(steps)
                break
            if x == 'L':
                curr = nodes[curr][0]
            elif x == 'R':
                curr = nodes[curr][1]
            steps += 1
    print(steps)
