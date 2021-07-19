with open("inputs/9.txt") as f:
    input = f.read()

numbers = list(map(int, input.split()))

for i in range(25, len(numbers)):
    match_found = False
    for n1 in numbers[i-25:i]:
        if match_found:
            break
        for n2 in numbers[i-25:i]:
            if n1 == n2:
                continue
            if n1 + n2 == numbers[i]:
                match_found = True
                break

    if not match_found:
        print("Part 1 answer:", numbers[i])
        break

expected_sum = 400480901 # part 1 answer

for i in range(len(numbers)):
    if numbers[i] == expected_sum:
        continue

    contiguous_set = [numbers[i]]
    current_index = i
    while sum(contiguous_set) < expected_sum:
        current_index += 1
        contiguous_set.append(numbers[current_index])

        if sum(contiguous_set) == expected_sum:
            print("Part 2 answer:", min(contiguous_set) + max(contiguous_set))
