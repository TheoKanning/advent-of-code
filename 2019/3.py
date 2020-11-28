def get_new_coords(x, y, direction):
    if direction == 'U':
        return x, y+1
    elif direction == 'D':
        return x, y-1
    elif direction == 'L':
        return x-1,y
    elif direction == 'R':
        return x+1,y

with open('inputs/3.txt') as f:
    data = [[(path[0], int(path[1:])) for path in line.strip().split(',')] for line in f.readlines()]

paths = [set(), set()]
path_lengths = [{}, {}]

for wire in [0, 1]:
    x, y, total_steps = 0, 0, 0
    for direction, steps in data[wire]:
        for i in range(steps):
            total_steps += 1
            x,y = get_new_coords(x, y, direction)
            paths[wire].add((x,y))
            if (x,y) not in path_lengths:
                path_lengths[wire][(x,y)] = total_steps

intersections = paths[0] & paths[1]
manhattan_distances = map(lambda x: abs(x[0]) + abs(x[1]), intersections)
print(f"Part 1 answer: {min(manhattan_distances)}")

total_path_lengths = map(lambda x: path_lengths[0][x] + path_lengths[1][x], intersections)
print(f"Part 2 answer: {min(total_path_lengths)}")

