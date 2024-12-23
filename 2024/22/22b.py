import sys

f = open(sys.argv[1])

nums = [int(n) for n in f.read().splitlines()]

def eval(n):
    res = n
    res = (res ^ (res*64)) % 16777216
    res = (res ^ (res // 32)) % 16777216
    res = (res ^ (res * 2048)) % 16777216
    return res

seqmap = {}
for num in nums:
    prices = [num % 10]
    for _ in range(2000):
        num = eval(num)
        prices.append(num%10)
    seqs = set()
    for i in range(len(prices)-4):
        a, b, c, d, e = prices[i:i+5]
        seq = (b-a, c-b, d-c, e-d)
        if seq in seqs: continue
        if seq not in seqmap: seqmap[seq] = 0
        seqs.add(seq)
        seqmap[seq] += e

print(max(seqmap.values()))


