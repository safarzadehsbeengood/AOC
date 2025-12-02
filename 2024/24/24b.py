f = open("input.txt")

wires, conns = f.read().split('\n\n')
wires = wires.splitlines()
conns = conns.splitlines()

z_output = []

x_input = []
for i in range(45):
    x_input.append('x'+str(i).rjust(2, '0'))
    z_output.append('z'+str(i).rjust(2, '0'))

y_input = []
for i in range(45):
    y_input.append('y'+str(i).rjust(2, '0'))

gates = {}

to_write = []

gates_and, gates_or, gates_xor = [], [], [] 
for line in conns:
    a, op, b, _, to = line.split()
    if op == 'AND': gates_and.append(to)
    if op == 'XOR': gates_or.append(to)
    if op == 'OR': gates_xor.append(to)

    to_write.append(f'{a} -> {to}; {b} -> {to};')

with open("pt2.txt", "w") as wf:
    wf.write(' -> '.join(sorted(x_input))+';')
    wf.write('\n\n')
    wf.write(' -> '.join(sorted(y_input))+';')
    wf.write('\n\n')

    wf.write('; '.join(gates_and)+';')
    wf.write('\n\n')
    wf.write('; '.join(gates_or)+';')
    wf.write('\n\n')
    wf.write('; '.join(gates_xor)+';')
    wf.write('\n\n')

    wf.write(' -> '.join(sorted(z_output))+';')
    wf.write('\n\n')

    wf.write('\n'.join(to_write))

