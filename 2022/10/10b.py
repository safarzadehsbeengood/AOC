from colorama import init, Fore
init(autoreset=True)
crt = ''

with open('input.txt', 'r') as input:
    x = 1
    cycle = 0
    ops = input.read().splitlines()
    for op in ops:
        cycle += 1
        if x <= cycle <= x+2:
            crt += '#'
        else:
            crt += '.'
        if cycle == 40:
            crt += ' '
            cycle = 0
            
        if op.startswith('addx'):
            cycle += 1
            if x <= cycle <= x+2:
                crt += '#'
            else:
                crt += '.'
            if cycle == 40:
                crt += ' '
                cycle = 0
            x += int(op.split()[1])
    
    result = crt.split()
    for row in result:
        print(row)