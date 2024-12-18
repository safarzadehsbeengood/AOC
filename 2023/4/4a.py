points = []

with open('input.txt', 'r') as input:
    lines = input.read().splitlines()

    for line in lines:
        matches = []
        winning = [int(number) for number in line.split(': ')[1].split(' | ')[0].split()]
        hand = [int(number) for number in line.split(': ')[1].split(' | ')[1].split()]
        for number in winning:
            if number in hand:
                matches.append(number)
        if not matches:
            continue
        if len(matches) == 1:
            points.append(1)
        else:
            power = len(matches) - 1
            points.append(2 ** power)

print(sum(points))
