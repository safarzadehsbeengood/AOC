with open('input.txt', 'r') as input:
    signal_strengths = []
    x = 1
    cycle = 1
    lines = input.read().splitlines()
    for line in lines:
        if line == 'noop':
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signal_strengths.append(cycle * x)
        else:
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signal_strengths.append(cycle * x)
            x += int(line.split()[1])
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                signal_strengths.append(cycle * x)

    print(sum(signal_strengths))
