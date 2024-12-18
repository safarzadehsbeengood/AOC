current_dir = root = '/'

with open('input.txt', 'r') as input:
    prompts = input.read().splitlines()
    path = '/home'
    dirs = {"/home": 0}
    for prompt in prompts[1:]:
        prompt = prompt.split()
        # $ commands
        if prompt[0] == '$':
            if prompt[1] == 'ls':
                continue
            elif prompt[1] == 'cd':
                if prompt[2] == '..':
                    path = path[:path.rindex('/')]
                else:
                    path += '/' + prompt[2]
                    dirs[path] = 0
        else:
            if prompt[0] != 'dir':
                temp_path = path
                while temp_path != "":
                    dirs[temp_path] += int(prompt[0])
                    temp_path = temp_path[:temp_path.rindex('/')]
    required_space = dirs['/home'] - (70000000 - 30000000)
    smallest_possible = dirs['/home']
    for _, size in dirs.items():
        if required_space < size < smallest_possible:
            smallest_possible = size
    print(smallest_possible)