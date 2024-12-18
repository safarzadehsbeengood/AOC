sections = []
engulfed = 0

with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    for line in lines:
        sections.append(((int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])), (int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1]))))
    for first_range, second_range in sections:
        # first in second
        if first_range[0] >= second_range[0] and first_range[1] <= second_range[1]:
            engulfed += 1
        # second in first
        elif second_range[0] >= first_range[0] and second_range[1] <= first_range[1]:
            engulfed += 1
    print(engulfed)
