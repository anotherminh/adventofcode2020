f = open('day16-input.txt').readlines()

rules_str = """departure location: 39-715 or 734-949
departure station: 30-152 or 160-959
departure platform: 34-780 or 798-955
departure track: 32-674 or 699-952
departure date: 38-55 or 74-952
departure time: 45-533 or 547-970
arrival location: 27-168 or 191-969
arrival station: 43-585 or 599-953
arrival platform: 40-831 or 837-961
arrival track: 37-293 or 301-974
class: 40-89 or 112-950
duration: 25-600 or 625-970
price: 45-318 or 341-954
route: 40-898 or 912-968
row: 38-872 or 881-958
seat: 37-821 or 831-958
train: 26-343 or 365-956
type: 37-857 or 872-960
wagon: 36-425 or 445-972
zone: 44-270 or 286-967"""

my_ticket = '223,139,211,131,113,197,151,193,127,53,89,167,227,79,163,199,191,83,137,149'

def parseRange(range_tuple):
    [start, end] = range_tuple
    return range(int(start), int(end) + 1)

def parseInput(rules, my_ticket, lines):
    parsed_rules = {}
    for rule in rules.split('\n'):
        [field_name, valid_range] = rule.split(':')
        [range1, range2] = [parseRange(r.strip().split('-')) for r in valid_range.split(' or ')]
        parsed_rules[field_name] = [range1, range2]
    nearby_tickets = []
    for l in lines:
        nearby_tickets.append([int(i) for i in l.strip().split(',')])
    my_ticket = [int(f) for f in my_ticket.split(',')]
    return [parsed_rules, my_ticket, nearby_tickets]


def isValidField(field, ranges):
    for _range in ranges:
        [r1, r2] = _range
        if (field in r1) or (field in r2):
            return True
    return False


def solve1(tickets):
    # find all the invalid values and add them up
    [rules, _, nearby_tickets] = parseInput(rules_str, my_ticket, tickets)
    ranges = rules.values()
    error_rate = 0
    for ticket in nearby_tickets:
        for field in ticket:
            if not isValidField(field, ranges):
                error_rate += field
    return error_rate

print(solve1(f))

# the possible solutions happen to be easy to crack
# no need to get fancy with different combinations
def solvePositions(all_pos):
    # each field should appear only once
    # sort by the most restrict fields
    all_pos = [[k, all_pos[k]] for k in all_pos]
    all_pos = sorted(all_pos, key=lambda v: len(v[1]))
    resolved_pos = {}
    taken_pos = set()
    for field, possible_positions in all_pos:
        remaining_position = list(filter(lambda x: x not in taken_pos, possible_positions))
        resolved_pos[field] = remaining_position[0]
        taken_pos.add(remaining_position[0])
    return resolved_pos

def solve2(rules, my_ticket, tickets):
    [rules, my_ticket, nearby_tickets] = parseInput(rules, my_ticket, tickets)
    fields = list(rules.keys())
    ranges = list(rules.values())
    nearby_tickets = list(filter(lambda t: all(isValidField(f, ranges) for f in t), nearby_tickets))
    possible_field_positions = {}
    while len(possible_field_positions.keys()) < len(fields):
        # determine the field at each position:
        for pos in range(len(nearby_tickets[0])):
            all_fields_at_pos = [t[pos] for t in nearby_tickets]
            for f in fields:
                allValid = all(isValidField(tf, [rules[f]]) for tf in all_fields_at_pos)
                if allValid:
                    if f in possible_field_positions:
                        possible_field_positions[f].append(pos)
                    else:
                        possible_field_positions[f] = [pos]
    field_positions = solvePositions(possible_field_positions)

    prefix = 'departure'
    departure_fields = list(filter(lambda f: f.startswith(prefix), fields))

    result = 1
    for v in departure_fields:
        result *= my_ticket[field_positions[v]]
    return result

exampleRules = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19"""

ex_my_ticket = "11,12,13"

exampleTickets = """3,9,18
15,1,5
5,14,9"""

# solve2(exampleRules, ex_my_ticket, exampleTickets.split('\n'))
solve2(rules_str, my_ticket, f)

