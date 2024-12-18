import sys
import re
from tqdm import tqdm

f = open(sys.argv[1], "r")

registers, program = f.read().split('\n\n')

f.close()

A, B, C = tuple(map(int, re.findall(r'\d+', registers)))
IP = 0

program = list(map(int, re.findall(r'\d', program)))

def eval_combo(n):
    global A, B, C
    match n:
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            return n

# funcs

# 0
def adv(combo):
    global IP, A
    denom = 1 << eval_combo(combo)
    A = A // denom
    IP += 2

# 1
def bxl(literal):
    global IP, B
    B = B ^ literal
    IP += 2

# 2
def bst(combo):
    global IP, B
    B = eval_combo(combo) % 8
    IP += 2

# 3
def jnz(literal):
    global IP, A
    if A == 0:
        IP += 2
        return
    IP = literal

# 4
def bxc(operand = None):
    global IP, B, C
    B = B ^ C
    IP += 2

# 5
def out(combo):
    global IP, A, B, C
    val = eval_combo(combo)
    # print(val % 8, end=',')
    IP += 2
    return val % 8

# 6
def bdv(combo):
    global IP, A, B
    denom = 1 << eval_combo(combo)
    B = A // denom
    IP += 2

# 7
def cdv(combo):
    global IP, A, C
    denom = 1 << eval_combo(combo)
    C = A // denom
    IP += 2

funcs = (adv, bxl, bst, jnz, bxc, out, bdv, cdv)
ops = {i: funcs[i] for i in range(8)}
print(f'A: {A} B: {B} C: {C}')
print(program)
print()

output = []
while IP < len(program):
    foo = funcs[program[IP]]
    if IP+1 >= len(program):
        if output[-1] != program[len(output)-1]:
            break
    if foo == out:
        res = foo(program[IP+1])
        output.append(res)
    else:
        foo(program[IP+1])
print(','.join(list(map(str, output))))
