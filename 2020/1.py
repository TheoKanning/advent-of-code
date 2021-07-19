with open("inputs/1.txt") as f:
    input = f.read()

entries = list(map(int, input.split('\n')))

import itertools

for combo in itertools.product(entries, entries):
    if sum(combo) == 2020:
        print("Part 1 answer:", combo[0]*combo[1])
        break

for combo in itertools.product(entries, itertools.product(entries, entries)):
    if combo[0] + combo[1][0] + combo[1][1] == 2020:
        print("Part 2 answer:", combo[0] * combo[1][0] * combo[1][1])
        break
