with open("inputs/8.txt") as f:
    input = f.read()

commands = list(map(lambda x: x.split(' '), input.split('\n')))

accumulator = 0
visited_indices = []
index = 0
while index not in visited_indices:
    visited_indices.append(index)
    command, value = commands[index]
    if command == 'nop':
        index += 1
    elif command == 'acc':
        accumulator += int(value)
        index += 1
    elif command == 'jmp':
        index += int(value)

print("Part 1 answer:", accumulator)


def terminates(commands):
    visited_indices = []
    index = 0
    accumulator = 0
    while True:
        visited_indices.append(index)
        command, value = commands[index]
        if command == 'nop':
            index += 1
        elif command == 'acc':
            index += 1
            accumulator += int(value)
        elif command == 'jmp':
            index += int(value)

        if index in visited_indices:
            return None
        if index == len(commands):
            return accumulator

import copy

for i in range(len(commands)):
    if commands[i][0] == 'acc':
        continue

    modified_commands = copy.deepcopy(commands)
    if commands[i][0] == 'jmp':
        modified_commands[i][0] = 'nop'
    elif commands[i][0] == 'nop':
        modified_commands[i][0] = 'jmp'

    result = terminates(modified_commands)
    if result is not None:
        print("Part 2 answer:", result)