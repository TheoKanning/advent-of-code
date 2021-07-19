with open("inputs/11.txt") as f:
    input = f.read()

# input = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""

seats = [[c for c in row] for row in input.split()]

def adjacent_squares(row, col, grid):
    row_min = max(0, row-1)
    row_max = min(len(grid)-1, row+1)
    col_min = max(0, col-1)
    col_max = min(len(grid[0])-1, col+1)

    contents = []

    for r in range(row_min,row_max+1):
        for c in range(col_min,col_max+1):
            if r == row and c == col:
                continue

            contents.append(grid[r][c])

    return contents

import copy

original_seats = copy.deepcopy(seats)
new_seats = copy.deepcopy(seats)

changed = True
while changed:
    changed = False

    for row in range(len(seats)):
        for col in range(len(seats[0])):
            current_state = original_seats[row][col]
            adjacents = adjacent_squares(row, col, original_seats)
            if current_state == 'L' and adjacents.count('#') == 0:
                new_seats[row][col] = '#'
                changed = True
            elif current_state == '#' and adjacents.count('#') >= 4:
                new_seats[row][col] = 'L'
                changed = True

    original_seats = copy.deepcopy(new_seats)

print("Part 1 answer:", sum(row.count('#') for row in new_seats))

def visible_seats(row, col, grid):
    import itertools
    directions = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    directions.remove((0, 0))

    neighbors = []
    for delta_row, delta_col in directions:
        r = row + delta_row
        c = col + delta_col
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] in ['#', 'L']:
                neighbors.append(grid[r][c])
                break
            r += delta_row
            c += delta_col

    return neighbors

original_seats = copy.deepcopy(seats)
new_seats = copy.deepcopy(seats)

changed = True
i = 0
while changed and i < 3:
    changed = False
    # i += 1

    for row in range(len(seats)):
        for col in range(len(seats[0])):
            current_state = original_seats[row][col]
            adjacents = visible_seats(row, col, original_seats)
            if current_state == 'L' and adjacents.count('#') == 0:
                new_seats[row][col] = '#'
                changed = True
            elif current_state == '#' and adjacents.count('#') >= 5:
                new_seats[row][col] = 'L'
                changed = True

    original_seats = copy.deepcopy(new_seats)
    for row in new_seats:
        print("".join(row))

    print('\n\n')


print("Part 2 answer:", sum(row.count('#') for row in new_seats))