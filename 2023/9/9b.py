import time
extrapolated = []

def extrapolate(x, sequences):
    v = []
    for i in range(len(x)-1):
        v.append(x[i+1]-x[i])
    sequences.append(v)
    if sum(v) == 0:
        return
    extrapolate(v, sequences)

with open('input.txt', 'r') as input:
    histories = [list(map(int, line.split())) for line in input.read().splitlines()]
    for history in histories:
        # print(history)
        sequences = [history]
        extrapolate(history, sequences)
        # for sequence in sequences:
        #     print(sequence)
        # print()

        # fill in vals
        sequences[-1].insert(0, 0)
        for i in range(len(sequences)-2, -1, -1):
            e = sequences[i][0] - sequences[i+1][0]
            sequences[i].insert(0, e)
        extrapolated.append(sequences[0][0])
        # for sequence in sequences:
        #     print(sequence)
        # print()

    print(sum(extrapolated))
