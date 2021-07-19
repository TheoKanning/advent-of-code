with open("inputs/2.txt") as f:
    input = f.readlines()

total_valid = 0

for entry in input:
    rule, password = entry.split(':')
    bounds, letter = rule.split(' ')
    lower_bound, upper_bound = bounds.split('-')

    if int(lower_bound) <= password.count(letter) <= int(upper_bound):
        total_valid += 1

print("Part 1 answer:", total_valid)


total_valid = 0

for entry in input:
    rule, password = entry.split(':')
    password = password.strip()
    indices, letter = rule.split(' ')
    first, second = indices.split('-')

    substring = password[int(first)-1] + password[int(second)-1]

    if substring.count(letter) ==1:
        total_valid += 1

print("Part 2 answer:", total_valid)