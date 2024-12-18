cards = {}

with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    for i in range(1, len(lines)+1):
        cards[i] = 1

    current_card = 1
    for line in lines:
        matches = []
        winning = [int(number) for number in line.split(': ')[1].split(' | ')[0].split()]
        hand = [int(number) for number in line.split(': ')[1].split(' | ')[1].split()]
        for number in winning:
            if number in hand:
                matches.append(number)
        for i in range(current_card+1, current_card + len(matches) + 1):
            cards[i] += cards[current_card]
        current_card += 1

for card, copies in cards.items():
    print(f'{card}:'.ljust(6) + f'{copies}')
print(sum(cards.values()))