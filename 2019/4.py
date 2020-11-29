minimum = 130254
maximum = 678275

passwords = []

for candidate in range(130254, 678275):
    number_str = str(candidate)
    has_double = False
    decreasing = False
    for i in range(0, 5):
        if number_str[i] == number_str[i+1]:
            has_double = True
        if number_str[i] > number_str[i+1]:
            decreasing = True
            break
    if has_double and not decreasing:
        passwords.append(candidate)

print(f"Part 1 answer: {len(passwords)}")

def has_exactly_two_consecutive(password):
    number_str = str(password)
    for group_size in range(6, 2, -1):
        for digit in range(0,10):
            number_str = number_str.replace(str(digit)*group_size, '')

    for digit in range(0,10):
        if str(digit)*2 in number_str:
            return True

    return False

part2_passwords = list(filter(has_exactly_two_consecutive, passwords))

print(f"Part 2 answer: {len(part2_passwords)}")

