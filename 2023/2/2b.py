from colorama import Fore

powers = []

with open("input.txt", 'r') as input:
    lines = input.read().splitlines()

    for line in lines:
        id = line.split(': ')[0].split()[1]
        games = line.split(': ')[1].split('; ')
        max_red = 0
        max_green = 0
        max_blue = 0
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
                if (num > max_red) and (color == 1):
                    max_red = num
                if (num > max_green) and (color == 2):
                    max_green = num
                if (num > max_blue) and (color == 3):
                    max_blue = num
        powers.append(max_red * max_green * max_blue)
        print(Fore.RED + str(max_red).ljust(4) + ' ' + Fore.GREEN + str(max_green).ljust(4) + ' ' + Fore.BLUE + str(max_blue).ljust(4) + ' ' + Fore.WHITE + line)
print(sum(powers))
        
