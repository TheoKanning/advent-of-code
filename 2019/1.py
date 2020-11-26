
with open('inputs/1.txt') as f:
    masses = list(map(int, f))

# Part 1
fuels = map(lambda x: x//3 - 2, masses)
print(f"Part 1 answer: {sum(fuels)}")

def get_fuel_part_2(mass):
    if (mass <= 6):
        return 0

    fuel = mass//3 - 2
    return fuel + get_fuel_part_2(fuel)

# Part 2
fuels = map(get_fuel_part_2, masses)
print(f"Part 2 answer: {sum(fuels)}")
