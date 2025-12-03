from aocd import get_data

data = get_data(day=3, year=2025).splitlines()

# test = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""
# data = test.splitlines()

res = 0

for bank in data:
    dig = max(bank)
    first_battery_idx = bank.find(dig)
    while int(dig) >= 0 and first_battery_idx == len(bank)-1:
        dig = str(int(dig)-1)
        first_battery_idx = bank.find(dig)
    first_battery = bank[first_battery_idx]
    second_battery = max(bank[first_battery_idx+1:])
    res += int(first_battery + second_battery)

print(res)


# pt 2
res = 0

def find_joltage(bank, batteries_left, current_batteries):
    if batteries_left == 0: return current_batteries
    max_in_bank = max(bank[:len(bank)-batteries_left+1])
    idx = bank.find(max_in_bank)
    return find_joltage(bank[idx+1:], batteries_left-1, current_batteries + max_in_bank)

for bank in data:
    joltage = find_joltage(bank, 12, '')
    res += int(joltage)

print(res)