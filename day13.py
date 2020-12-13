import re

example_ts, example_bus_str = open('day13-example.txt').readlines()
ts, bus_str = open('day13-input.txt').readlines()

def parseBusNum(bus_str):
    if len(re.findall("\d+", bus_str)) > 0:
        return int(bus_str)
    else:
        return None

def parseBusStr(bus_str, include_none = False):
    buses = []
    for bus in bus_str.split(','):
        parsed = parseBusNum(bus)
        if parsed != None or include_none:
            buses.append(parsed)
    return buses

def solvePart1(ts, bus_str):
    buses = parseBusStr(bus_str)
    earliest_ts = None
    earliest_bus_id = None
    for bus in buses:
        if ts % bus == 0:
            print('0')
            return 0
        else:
            bus_arrival = ((ts // bus) + 1) * bus
            if earliest_ts == None or ((bus_arrival - ts) < earliest_ts):
                earliest_bus_id = bus
                earliest_ts = bus_arrival - ts

    return earliest_bus_id * earliest_ts


print(solvePart1(int(example_ts), example_bus_str))
print(solvePart1(int(ts), bus_str))

# finds the least common multiple
# then use this for our step size
def lcm(nums):
    res = nums[0]
    for n in nums:
        res = (res * n) // gcd(res, n)
    return res

# finds the greatest common divisor to calculate the lcm
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def solvePart2(bus_str, start_at = 0):
    buses = parseBusStr(bus_str, True)
    bus_offsets = {}
    for idx in range(len(buses)):
        if buses[idx] != None:
            bus_offsets[buses[idx]] = idx
    buses = [b for b in bus_offsets]

    solved_ts = None
    start_ts = (start_at // buses[0]) * buses[0]
    step_size = buses[0]
    while solved_ts == None:
        print('start_ts', start_ts)
        solved_ts = start_ts
        for bus in buses:
            target_departure = start_ts + bus_offsets[bus]
            if target_departure % bus == 0:
                step_size = lcm([step_size, bus])
            if target_departure % bus != 0:
                solved_ts = None
                start_ts += step_size
                break
    return solved_ts


print(solvePart2(example_bus_str))
print(solvePart2(bus_str, 100000000000000))
