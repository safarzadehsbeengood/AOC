from tqdm import tqdm
monkey_items = {}
monkey_inspections = {}
with open('input.txt', 'r') as input:
    monkeys = [monkey.split('\n') for monkey in input.read().split('\n\n')]
    for i, monkey in enumerate(monkeys): 
        monkey_items[i] = list(map(int, monkey[1].split(': ')[1].split(', ')))
        monkey_inspections[i] = 0
        # print(monkey)
        # print()

    for x in tqdm(range(20)):
        for i, monkey in enumerate(monkeys):
            # print(f'Monkey {i}:')
            op = monkey[2].strip().split(': ')[1].split('new = ')[1]
            exp = op.split()
            first = exp[0]
            second = exp[2]
            op = exp[1]
            test = int(monkey[3].split()[-1])
            true_case = int(monkey[4].split()[-1])
            false_case = int(monkey[5].split()[-1])
            # print(f'Monkey {i}: {first} {op} {second}')
            for item in monkey_items[i]:
                # print(monkey_items[i])
                a = item if first == 'old' else int(first)
                b = item if second == 'old' else int(second)
                if op == '*':
                    res = (a * b) // 3
                    # print(f'    {a} {op} {b} == {a*b} // 3 = {res}')
                elif op == '+':
                    res = (a + b) // 3
                    # print(f'    {a} {op} {b} == {a*b} // 3 = {res}')
                if res % test == 0:
                    # print(f'    {res} // {test} == {(res % test == 0)} -> Monkey {true_case}')
                    monkey_items[true_case].append(res)
                else:
                    # print(f'    {res} // {test} == {(res % test == 0)} -> Monkey {false_case}')
                    monkey_items[false_case].append(res)
                monkey_inspections[i] += 1
                # print()
            monkey_items[i].clear()
    print(monkey_inspections)
    all_inspections = sorted(monkey_inspections.values())
    print(all_inspections[-1] * all_inspections[-2])

            

            



