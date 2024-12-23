import sys

f = open(sys.argv[1])

nums = [int(n) for n in f.read().splitlines()]

print(nums)

pt1 = 0
for num in nums:
    res = num
    for _ in range(2000):
        res = (res ^ (res*64)) % 16777216
        res = (res ^ (res // 32)) % 16777216
        res = (res ^ (res * 2048)) % 16777216
    # print(res)
    pt1 += res

print(pt1)

