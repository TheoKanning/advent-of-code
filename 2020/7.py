with open("inputs/7.txt") as f:
    input = f.read()

rules = {}

for rule in input.split('\n'):
    bag_name = rule.split("bags contain")[0].strip()
    contents = rule.split("bags contain")[1].strip()

    rules[bag_name] = {}

    if contents == "no other bags.":
        continue

    contents = contents.replace(',', '').replace('.', '').replace('bags', 'bag').strip()

    for sub_bag in contents.split('bag'):
        if len(sub_bag) == 0:
            continue

        sub_bag = sub_bag.strip()
        sub_bag_quantity = int(sub_bag[0])
        sub_bag_name = sub_bag[2:]
        rules[bag_name][sub_bag_name] = sub_bag_quantity

part_one_bags = ["shiny gold"]
changed = True

while changed:
    changed = False
    for bag in rules.keys():
        if bag in part_one_bags:
            continue

        if any(sub_bag in part_one_bags for sub_bag in rules[bag].keys()):
            part_one_bags.append(bag)
            changed = True

def child_bags(bag_name, rules):
    total = 0
    for child in rules[bag_name]:
        total += rules[bag_name][child] * (1 + child_bags(child, rules))

    return total


print("Part 1 answer:", len(part_one_bags)-1)

print("Part 2 answer:", child_bags("shiny gold", rules))
