import re

def show():
    for stack, items in stacks.items():
        print(f'{stack}: {items}')

def move(amount, source, dest):
    for i in range(amount):
        crate = stacks[source].pop()
        stacks[dest].append(crate)

with open('input.txt', 'r') as input:
    crates, directions = input.read().split('\n\n')
    crates = crates.splitlines()
    n = len(crates.pop().split()) # number of stacks
    stacks = {}
    for i in range(1, n+1):
        stacks[i] = []
    directions = directions.splitlines()

    instructions = []
    for instruction in directions:
        a = instruction.split()
        instructions.append((int(a[1]), int(a[3]), int(a[5])))

    # load initial crates
    current_crate = 1
    for j in range(1, len(crates[0]), 4):
        for i in range(len(crates)-1, -1, -1):
            if crates[i][j] != ' ':
                stacks[current_crate].append(crates[i][j])
        current_crate += 1
    show()
    for n, s, d in instructions:
        move(n, s, d)
    show()

    message = []
    for stack in stacks.values():
        message.append(stack[-1])
    print(''.join(message))