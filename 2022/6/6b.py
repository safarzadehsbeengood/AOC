with open('input.txt', 'r') as input:
    string = input.read().replace('\n', '')
    # string = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    i = 13
    while i < len(string) and len(set(string[i-13:i+1])) < 14:
        i += 1
        # print(string[i-13:i+1])
    print(i+1)