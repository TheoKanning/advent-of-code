with open("inputs/10.txt") as f:
    input = f.read()

adapters = list(map(int, input.split()))

adapters.sort()
adapters.append(adapters[-1] + 3)

jumps = []
current_joltage = 0

for joltage in adapters:
    jumps.append(joltage - current_joltage)
    current_joltage = joltage

print("Part 1 answer:", jumps.count(1) * jumps.count(3))

total_routes = {0: 1}

for joltage in adapters:
    routes = 0
    for sub_joltage in range(joltage - 3, joltage):
        if sub_joltage in total_routes.keys():
            routes += total_routes[sub_joltage]
    total_routes[joltage] = routes

print("Part 2 answer:", total_routes[max(adapters)])
