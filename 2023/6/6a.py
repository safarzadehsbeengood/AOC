from colorama import Fore, init
import numpy as np
init(autoreset=True)

times = []
distances = []
wins = {}


with open('input.txt', 'r') as input:
    lines = input.read().splitlines()

    times = [int(time) for time in lines[0].split(':')[1].strip().split()]
    distances = [int(distance) for distance in lines[1].split(':')[1].strip().split()]
    # print(times)
    # print(distances)

    # calculate winning button holds
    for race, time in enumerate(times):
        possible = {}
        distance_to_beat = distances[race]
        # print(f'Race {race}: {time} -> {distance_to_beat}ms')
        for i in range(1, time):
            # after holding the button for i ms,
            speed = i
            # the distance ot travel becomes distance - i
            time_to_travel = time - i

            possible[i] = time_to_travel * speed
        # print(f'Race {race}:')
        race_wins = []
        for time_held, distance in possible.items():
            if distance >= distance_to_beat:
                race_wins.append(time_held)
        wins[race] = race_wins
            # print(f'{time_held}ms:'.ljust(8) + f'{distance}'.rjust(6) + 'mm')

    ways_to_win = []
    for held_times in wins.values():
        ways_to_win.append(len(held_times))
    print(np.prod(ways_to_win))