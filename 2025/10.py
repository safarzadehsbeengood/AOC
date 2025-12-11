from aocd import get_data
import collections
import z3

data_source = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

data_source = get_data(day=10, year=2025)

def button_to_bitmask(btn, size):
    res = ["0"]*size
    for b in btn:
        res[b] = "1"
    res = int(''.join(res), 2)
    return res
    

data = data_source.splitlines()
p1 = 0
p2 = 0
for case in data:
    case = case.split()
    lights, button_tuples, joltages = case[0], list(map(eval, case[1:-1])), [int(x) for x in case[-1][1:-1].split(",")]
    button_tuples = [btn if type(btn) == tuple else (btn,) for btn in button_tuples]
    # get target lights
    target = int(lights[1:-1].replace("#", "1").replace('.', "0"), 2)

    # convert buttons to bitmasks
    masks = [button_to_bitmask(btn, len(lights)-2) for btn in button_tuples]

    d = {}
    q = collections.deque()
    d[0] = 0 # no button presses for 0 state
    q.append(0) # starting state

    while len(q) > 0:
        curr = q.popleft()
        if curr == target:
            p1 += d[target]
            break
    
        # explore next candidate states
        # if haven't seen state before, inc and add to queue
        for m in masks:
            if (curr ^ m) not in d:
                d[curr ^ m] = d[curr] + 1
                q.append(curr ^ m)
    
    V = []
    for i in range(len(masks)):
        V.append(z3.Int(f"B{i}"))
    EQ = []
    for i in range(len(joltages)):
        terms = []
        for j in range(len(button_tuples)):
            if i in button_tuples[j]:
                terms.append(V[j])
        eq = (sum(terms) == joltages[i])
        EQ.append(eq)
    o = z3.Optimize()
    o.minimize(sum(V))
    for eq in EQ:
        o.add(eq)
    for v in V:
        o.add(v >= 0)
    assert o.check()
    M = o.model()
    for d in M.decls():
        p2 += M[d].as_long()
        
print(p1)
print(p2)

# pt 2

pt2 = 0
     
    