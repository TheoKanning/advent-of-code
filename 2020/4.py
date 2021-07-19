with open("inputs/4.txt") as f:
    input = f.read()

passports = [dict(map(lambda x: x.split(':'), passport.split())) for passport in input.split('\n\n')]

required_fields = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
}

valid_passports = 0
for passport in passports:
    if passport.keys() >= required_fields:
        valid_passports += 1

print("Part 1 answer: ", valid_passports)


def valid_number(number, minimum, max):
    if len(number) != 4:
        return False

    return minimum <= int(number) <= max

def valid_height(height):
    if height.endswith('in'):
        height = height.replace('in', '')
        return 59 <= int(height) <= 76
    elif height.endswith('cm'):
        height = height.replace('cm', '')
        return 150 <= int(height) <= 193
    return False

def valid_hair_color(hair_color):
    import re
    return re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hair_color)

def valid_eye_color(eye_color):
    return eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_passport_id(passport_id):
    return len(passport_id) == 9 and passport_id.isdigit()

valid_passports = 0
for passport in passports:
    if not passport.keys() >= required_fields:
        continue

    if valid_number(passport['byr'], 1920, 2002) \
            and valid_number(passport['iyr'], 2010, 2020) \
            and valid_number(passport['eyr'], 2020, 2030) \
            and valid_height(passport['hgt']) \
            and valid_hair_color(passport['hcl']) \
            and valid_eye_color(passport['ecl']) \
            and valid_passport_id(passport['pid']):
        valid_passports += 1

print("Part 2 answer:", valid_passports)
