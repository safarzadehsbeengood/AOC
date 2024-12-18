import numpy as np
with open('input.txt', 'r') as input:
    total_calories = []
    elf_calories = [calories.split('\n') for calories in input.read().split("\n\n")]
    elf_calories[-1].pop()
    for calories in elf_calories:
        for i in range(len(calories)):
            calories[i] = int(calories[i])
    # print(elf_calories)
    for calories in elf_calories:
        total_calories.append(sum(calories))
    # print(total_calories)
    print(max(total_calories))
    print(sum(sorted(total_calories)[-3:]))