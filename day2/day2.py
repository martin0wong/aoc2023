import math
import re
from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

possible_games = 0
power_sum = 0
for line in lines:
    sets = re.sub("[;,:]", "", line).split()
    colormax = defaultdict(int)

    for count, color in zip(sets[2::2], sets[3::2]):
        colormax[color] = max(colormax[color], int(count))

    power = math.prod(colormax.values())
    if colormax["red"] <= 12 and colormax["green"] <= 13 and colormax["blue"] <= 14:
        possible_games += int(sets[1])
    power_sum += power

# Part 1
print(possible_games)

# Part 2
print(power_sum)