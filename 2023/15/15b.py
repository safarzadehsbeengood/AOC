def hash(s):
    x = 0
    for c in s:
        x += ord(c)
        x *= 17
        x %= 256
    return x

with open('input.txt', 'r') as input:  
    strings = input.read().split(',')
    # print(strings)
    # print('\n'.join(strings))
    boxes = {i: [] for i in range(256)}
    for string in strings:
        if '=' in string:
            label, fl = string.split('=')
            box = hash(label)
            spots = [i for i in range(len(boxes[box])) if label in boxes[box][i]]
            if spots:
                boxes[box][spots[0]] = label + ' ' + fl
            else:
                boxes[box].append(label + ' ' + fl)
        else:
            box = hash(string[:-1])
            spots = [i for i in range(len(boxes[box])) if string[:-1] in boxes[box][i]]
            # print(f'spots for {label}: {spots}')
            if spots:
                boxes[box].pop(spots[0])
            else:
                continue
    total = 0
    for box, l in boxes.items():
        if l:
            for i, slot in enumerate(l):
                fl = l[i].split()[1]
                fp = (box+1) * (i+1) * int(fl)
                total += fp
    print(total)