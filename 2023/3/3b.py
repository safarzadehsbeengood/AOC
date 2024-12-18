from colorama import init, Fore
import numpy as np
init(autoreset=True)
symbols = []
parts = []
partIndexes = []
gear_ratios = []
stars = {}

def isPartNumber(row, columnStart, columnEnd, lines) -> bool:
    # above and below
    for i in range(columnStart-1, columnEnd + 2):
        if (i >= 0) and (i < len(lines[0])-1):
            # above
            if (row != 0) and (lines[row-1][i] in symbols):
                return True 
            # below
            if (row != len(lines)-1) and (lines[row+1][i] in symbols):
                return True
    # left and right
    if columnStart > 0 and (lines[row][columnStart-1] in symbols) :
        return True
    if columnEnd < len(lines[0]) - 1 and (lines[row][columnEnd+1] in symbols):
        return True
    # print("NOT")
    return False

with open('input.txt', 'r') as input:
    lines = input.read().splitlines()
    line_length = len(lines[0])

    # collect symbols
    for line in lines:
        for c in line:
            # print(c)
            if not c.isalnum() and not c == '.':
                if not c in symbols:
                    symbols.append(c)
    
    # print(isPartNumber(10, 8, 10, lines))
    for line_number, line in enumerate(lines):
        # print(f'{line_number}: {line}')
        num = []
        i = 0
        x = 0
        while i < len(line):
            if line[i].isnumeric():
                j = i
                while j < len(line) and line[j].isnumeric():
                    num.append(line[j])
                    j += 1
                x = int(''.join(num))
                # print(str(x).ljust(15) + Fore.RED + 'row ' + Fore.WHITE + f'{line_number+1}'.ljust(20) + f'[{i}][{j}]'.rjust(10) + f' -> {isPartNumber(line_number, i, j, lines)}')
                if (isPartNumber(line_number, i, j-1, lines)):
                    parts.append(x)
                    partIndexes.append((x, line_number, i, j-1))
                i += len(num)
                num.clear()

            else:
                i += 1
                continue
    
    # part 2
    # collect star indices
    def partIsNeighbor(part: tuple, star: tuple) -> bool:
        # part -> (number, row, start_idx, end_idx)
        # star -> (row, column)
        if (star[0]-1 <= part[1] <= star[0]+1):
            for i in range(part[2], part[3]+1):
                if star[1]-1 <= i <= star[1]+1:
                    return True
        return False

    for line_number, line in enumerate(lines):
        for i in range(len(line)):
            if line[i] == '*':
                stars[(line_number, i)] = []
    
    for part in partIndexes:
        for star in stars.keys():
            if partIsNeighbor(part, star):
                stars[star].append(part[0])

    for star, parts in stars.items():
        # print(f'{star}'.ljust(10) + ': ' + f'{parts}')
        if len(parts) == 2:
            gear_ratios.append(parts[0] * parts[1])
    # print(gear_ratios)
    print(sum(gear_ratios))
        
