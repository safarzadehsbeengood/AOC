from aocd import get_data
import math

data_source = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

data_source = get_data(day=8, year=2025)

junctions = [tuple(map(int, j.split(','))) for j in data_source.splitlines()]

def distance(a, b):
    return math.dist(a, b)

dists = {}

for i in range(len(junctions)):
    for j in range(i+1, len(junctions)):
        dists[(i, j)] = distance(junctions[i], junctions[j])
dists = sorted(dists.items(), key=lambda x: x[1])

    
circuits = [set((tup,)) for tup in junctions.copy()]
circuits_pt2 = circuits.copy()

def connect_junctions(a, b):
    # find the circuits that a and b are in
    a_circuit, b_circuit = None, None
    for i, circuit in enumerate(circuits):
        if a in circuit: 
            a_circuit = i
        if b in circuit:
            b_circuit = i
    if a_circuit == b_circuit: return # same circuit
    # remove both of them and add the union back to circuits
    if a_circuit > b_circuit:
        a_circuit = circuits.pop(a_circuit)
        b_circuit = circuits.pop(b_circuit)
    else:
        b_circuit = circuits.pop(b_circuit)
        a_circuit = circuits.pop(a_circuit)
    circuits.append(a_circuit.union(b_circuit))
    if len(circuits) == 1:
        return a[0] * b[0]

pt_2 = None # for pt 2
for (i, j,), d in dists:
    a, b = junctions[i], junctions[j]
    res = connect_junctions(a, b)
    if res != None and pt_2 == None:
        pt_2 = res

circuit_lens = sorted([len(c) for c in circuits], reverse=True)

print(math.prod(circuit_lens[:3]))
print(pt_2)
        

# for (i, j,), d in dists:
    # print(junctions[i], junctions[j], d)