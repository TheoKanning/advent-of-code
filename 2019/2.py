def calculate_opcode(value1, value2):
    with open('inputs/2.txt') as f:
        data = f.read().split(',')
        data = list(map(int, data))

    # fix gravity assist
    data[1] = value1
    data[2] = value2

    for i in range(0, len(data)-3, 4):
        opcode = data[i]
        if opcode == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif opcode == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        elif opcode == 99:
            break

    return data[0]

print(f"Part 1 answer: {calculate_opcode(12, 2)}")

for noun in range(100):
    for verb in range(100):
        if calculate_opcode(noun, verb) == 19690720:
            print(f"Part 2 answer: {100*noun + verb}")
            break
