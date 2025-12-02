import sys

f = open(sys.argv[1])

wires, conns = f.read().split('\n\n')
print(wires)
print()
print(conns)

known = {}
values = {}

for line in wires.splitlines():
    wire, value = line.split(': ')
    known[wire] = int(value)


gates = {}

for line in conns.splitlines():
    a, op, b, _, to = line.split()
    gates[to] = (op, a, b)

ops = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b
}

print(gates)

def eval(wire):
    if wire in known: return known[wire]
    op, a, b = gates[wire]
    known[wire] = ops[op](eval(a), eval(b))
    return known[wire]

z = []
i = 0

while True:
    k = 'z' + str(i).rjust(2, '0')
    if k not in gates: break
    z.append(eval(k))
    i += 1

res = int(''.join(list(map(str, z[::-1]))), 2)

print(res)

