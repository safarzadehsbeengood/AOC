with open('input.txt', 'r') as input:
    string = input.read().replace('\n', '')
    # string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    i = 3
    while i < len(string) and len(set(string[i-3:i+1])) < 4:
        i += 1
        print(string[i-3:i+1])
    print(i+1)