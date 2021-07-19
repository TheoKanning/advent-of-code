with open("inputs/6.txt") as f:
    input = f.read()

groups = [group.split() for group in input.split('\n\n')]

total_answers = 0
for group in groups:
    total_answers += len(set(''.join(group)))

print("Part 1 answer:", total_answers)

total_answers = 0
for group in groups:
    sets = list(map(set, group))
    total_answers += len(sets[0].intersection(*sets))

print("Part 2 answer:", total_answers)