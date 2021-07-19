with open("inputs/5.txt") as f:
    input = f.read().replace('B', '1')\
        .replace('F', '0')\
        .replace('R', '1')\
        .replace('L', '0')

pass_ids = list(map(lambda x: int(x, 2), input.split('\n')))

print("Part 1 answer:", max(pass_ids))

for id in range(2**10):
    if id in pass_ids:
        continue

    if id+1 in pass_ids and id-1 in pass_ids:
        print("Part 2 answer:", id)
        break