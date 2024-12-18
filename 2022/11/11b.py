from tqdm import tqdm
monkeys = []
monkey_inspections = {}
with open('input.txt', 'r') as input:
    for line in input.read().strip().split('\n\n'):
        lines = line.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(': ')[1].split(', '))))
        monkey.append(eval("lambda old:" + lines[2].split('=')[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)
    counts = [0] * len(monkeys)

    # supermod
    mod = 1
    for monkey in monkeys:
        print(monkey)
        mod *= monkey[2]
    
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= mod 
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[i] += len(monkey[0])
            monkey[0] = []
    counts.sort()
    print(counts[-1] * counts[-2])
                
