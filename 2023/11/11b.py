from colorama import Fore, init
init(autoreset=True)
with open('input.txt', 'r') as input:
    # preprocessing
    lines = input.read().splitlines()
    grid = [[*line] for line in lines]
    empty_rows = [r for r, row in enumerate(lines) if all(ch == '.' for ch in row)]
    empty_cols = [c for c, col in enumerate(zip(*lines)) if all(ch == '.' for ch in col)]

    galaxies = [(r, c) for r ,row in enumerate(lines) for c, ch in enumerate(row) if ch == '#']
    # for row in grid: print(''.join(row))

    total = 0
    scale = 1000000
    
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                total += scale if r in empty_rows else 1
            for c in range(min(c1, c2), max(c1, c2)):
                total += scale if c in empty_cols else 1

    print(total)
