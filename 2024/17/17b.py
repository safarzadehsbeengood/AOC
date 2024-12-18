import sys
import re

f = open(sys.argv[1], "r")

_, program = f.read().split('\n\n')

f.close()

program = list(map(int, re.findall(r'\d', program)))
print(program)

def eval(input, ans):
    if input == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = 0
        c = 0
        out = None
        adv3 = False
        def combo(op):
            if 0 <= op <= 3: return op
            if op == 4: return a
            if op == 5: return b
            if op == 6: return c
            else:
                raise RuntimeError
        for p in range(0, len(program)-2, 2):
            ins = program[p]
            op = int(program[p+1])
            if ins == 0:
                assert not adv3
                assert op == 3
                adv3 = True
            elif ins == 1:
                b = b ^ op
            elif ins == 2:
                b = combo(op) % 8
            elif ins == 3:
                raise AssertionError
            elif ins == 4:
                b = b ^ c
            elif ins == 5:
                assert out is None
                out = combo(op) % 8
            elif ins == 6:
                b = a >> combo(op)
            elif ins == 7:
                c = a >> combo(op)
            if out == input[-1]:
                sub = eval(input[:-1], a)
                if sub is None: continue
                return sub
print(eval(program, 0))



            

