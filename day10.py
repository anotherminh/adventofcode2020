lines = list(map(lambda l: int(l.strip()), open('day10-input.txt').readlines()))

def solvePart1():
    current_jolt = 0
    sorted_adapters = sorted(lines)
    print(sorted_adapters)
    differences = { 1: 0, 2: 0, 3: 1 }
    for adapter in sorted_adapters:
        differences[adapter - current_jolt] += 1
        current_jolt = adapter
    return differences[1] * differences[3]

print(solvePart1())

# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0) 1 4 5 (8)
def countArrangements(adapters, memo):
    # print('adapters', adapters)
    if len(adapters) <= 1:
        return 1
    else:
        # take the current idx, but also try to skip it?
        count = 0
        first = adapters[0]
        for idx in range(1, 4):
            if idx < len(adapters) and (adapters[idx] - first) <= 3:
                # print(first, idx, adapters[idx])
                if adapters[idx] in memo:
                    count += memo[adapters[idx]]
                else:
                    res = countArrangements(adapters[idx:], memo)
                    memo[adapters[idx]] = res
                    count += res
        return count

# print(countArrangements([0, 1, 3, 5, 8], {}))
# print(countArrangements([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22], {}))
print(countArrangements([0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 49+3], {}))

def solvePart2():
    adapters = set(lines)
    sorted_adapters = sorted(lines)
    return countArrangements([0] + sorted_adapters + [sorted_adapters[-1] + 3], {})

print(solvePart2())
