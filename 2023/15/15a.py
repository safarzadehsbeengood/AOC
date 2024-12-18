with open('input.txt', 'r') as input:
    strings = input.read().split(',')
    # print('\n'.join(strings))
    total = 0
    for string in strings:
        x = 0
        for c in string:
            x += ord(c)
            x *= 17
            x %= 256
            # print(x)
        total += x
        # print(string, x)
    print(total)