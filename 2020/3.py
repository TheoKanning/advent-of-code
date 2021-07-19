with open("inputs/3.txt") as f:
    input = f.read()

trees = input.split('\n')
tree_width = len(trees[0])
tree_length = len(trees)

total_trees = 0
for y in range(tree_length):
    x = y * 3 % tree_width
    if trees[y][x] == '#':
        total_trees += 1

print("Part 1 answer:", total_trees)

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

part2_product = 1
for x_step, y_step in slopes:
    total_trees = 0
    for y in range(0, tree_length, y_step):
        x = (y // y_step) * x_step % tree_width
        if trees[y][x] == '#':
            total_trees += 1

    part2_product *= total_trees

print("Part 2 answer:", part2_product)