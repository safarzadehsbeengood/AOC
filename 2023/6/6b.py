from colorama import Fore, init
import numpy as np
from tqdm import tqdm
init(autoreset=True)

times = []
distances = []
wins = {}


with open('input.txt', 'r') as input:

    lines = input.read().splitlines()

    time = [time for time in lines[0].split(':')[1].strip().split()]
    time = int(''.join(time))
    distance = [distance for distance in lines[1].split(':')[1].strip().split()]
    distance = int(''.join(distance))
    print(time)
    print(distance)

    # calculate winning button holds
    possible = {}
    for i in tqdm(range(1, time)):
        # after holding the button for i ms,
        speed = i
        # the distance ot travel becomes distance - i
        time_to_travel = time - i

        possible[i] = time_to_travel * speed
    race_wins = []
    for time_held, distance_traveled in possible.items():
        if distance_traveled >= distance:
            race_wins.append(time_held)
    print(len(race_wins))