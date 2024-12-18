sections = []
overlapped = 0

with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    for line in lines:
        sections.append(((int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])), (int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1]))))
    for first_range, second_range in sections:
        fs, fe, ss, se = first_range[0], first_range[1], second_range[0], second_range[1]

        for i in range(fs, fe + 1):
            if i in range(ss, se+1):
                overlapped += 1
                break
    print(overlapped)
