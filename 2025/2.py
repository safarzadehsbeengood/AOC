from aocd import get_data

def is_valid(n: str):
    def is_repeating(window_size):
        if len(n) % window_size != 0: return False
        sections = [n[i:i+window_size] for i in range(0, len(n)-window_size+1, window_size)]
        set_sections = set(sections)
        # part 1 V
        # if len(sections) == 1 and window_size == len(n) // 2:
        # part 2 V
        if len(set_sections) == 1:
            return True
        return False
    window_size = len(n) // 2
    while window_size > 0:
        if is_repeating(window_size):
            return False
        window_size -= 1
        while window_size > 0 and len(n) % window_size != 0:
            window_size -= 1
        
    return True

data = [rng.split('-') for rng in get_data(day=2, year=2025).split(',')]
# test = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
# data = [rng.split('-') for rng in test.split(',')]

res = 0

for start, end in data:
    for num in range(int(start), int(end)+1):
        if not is_valid(str(num)):
            res += num
print(res)

