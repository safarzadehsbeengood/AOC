from colorama import Fore

possible = []

with open("input.txt", 'r') as input:
    lines = input.read().splitlines()

    for line in lines:
        is_possible = True
        id = line.split(': ')[0].split()[1]
        games = line.split(': ')[1].split('; ')
        for game in games:
            cubes = game.split(', ')
            for cube in cubes:
                color = 0
                if cube.find('red') >= 0:
                    color = 1
                elif cube.find('green') >= 0:
                    color = 2
                elif cube.find('blue') >= 0:
                    color = 3
                num = int(cube.split()[0])
                if (num > 12) and (color == 1):
                    is_possible = False
                    break
                if (num > 13) and (color == 2):
                    is_possible = False
                    break
                if (num > 14) and (color == 3):
                    is_possible = False
                    break
        if is_possible:
            possible.append(int(id))
    
print(sum(possible))
        
