import re
lines = open('day7-input.txt').readlines()
# lines = open('example.txt').readlines()

def cleanStr(rule):
    rule = rule.strip()
    if 'contains' in rule:
        return rule.split('contains ')
    else:
        return rule.split('contain ')

def removeCount(bag_desc):
    return re.sub('\d+', '', bag_desc)

def findOuterBag(s):
    match = re.search(r'^(.*?) bags', s)
    if match:
        return match.group(1)
    else:
        return match

def findInnerBags(s):
    return re.search(r'\d+ (.*?) bag', s).group(1)

print(findInnerBags('5 dark green bags'))
print(findInnerBags('5 light gray bags'))
print(findOuterBag('light beighe bags contain'))

def solveDay7():
    bag_rules = {}
    for rule in lines:
        bags = rule.split('contain ')
        outer_bag = findOuterBag(bags[0])
        inner_bags = []
        if 'no other bags' not in bags[1]:
            for b in bags[1].split(', '):
                inner_bags.append(findInnerBags(b))

        # the bags that can contain these bags
            for bag in inner_bags:
                if bag in bag_rules:
                    bag_rules[bag].append(outer_bag)
                else:
                    bag_rules[bag] = [outer_bag]

    solution = set()
    to_traverse = bag_rules['shiny gold']

    while len(to_traverse) > 0:
        last_el = to_traverse.pop()
        solution.add(last_el)
        if last_el in bag_rules:
            to_traverse += bag_rules[last_el]

    return solution

def findInnerBagsWithCount(s):
    match = re.search(r'(\d+) (.*?) bag', s)
    return [match.group(1), match.group(2)]

def solveDay7Part2():
    bag_rules = {}
    for rule in lines:
        bags = rule.split('contain ')
        outer_bag = findOuterBag(bags[0])
        inner_bags = []
        if 'no other bags' not in bags[1]:
            for b in bags[1].split(', '):
                inner_bags.append(findInnerBagsWithCount(b))

        bag_rules[outer_bag] = inner_bags

    solution = 0
    bag_count = {}
    to_traverse = bag_rules['shiny gold']

    while len(to_traverse) > 0:
        count, bag_name = to_traverse.pop()
        if bag_name in bag_count:
            bag_count[bag_name] += int(count)
        else:
            bag_count[bag_name] = int(count)
        solution += int(count)
        if bag_name in bag_rules:
            children = bag_rules[bag_name]
            total_children = []
            for c, n in children:
                total_children.append([int(count) * int(c), n])

            to_traverse += total_children

    other_count = 0
    for k, v in bag_count.items():
        other_count += v
    return solution


print(solveDay7Part2())
