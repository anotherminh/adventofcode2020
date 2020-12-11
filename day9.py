lines = list(map(lambda l: int(l.strip()), open('day9-input.txt').readlines()))

def is_valid(num, preamble):
    seen = set()
    for n in preamble:
        print(n, num, num -n, seen)
        if (num - n) in seen:
            return True
        else:
            seen.add(n)
    return False


def solvePart1():
    preamble = lines[0:25]
    msg = lines[25:]
    print('msg', msg)
    for num in msg:
        print('preamble', preamble)
        print('num', num)
        if is_valid(num, preamble):
            preamble = preamble[1:]
            preamble.append(num)
        else:
            print('Found invalid')
            return num
    return None

part1Answer = solvePart1()
print(part1Answer)

def solvePart2():
    start = 0
    end_idx = start + 1
    curr_sum = lines[start] + lines[end_idx]
    targetSum = part1Answer

    while end_idx < len(lines) and curr_sum != targetSum:
        if curr_sum < targetSum:
            end_idx += 1
            curr_sum += lines[end_idx]
        elif curr_sum > targetSum:
            curr_sum -= lines[start]
            start += 1
    if curr_sum == targetSum:
        sorted_set = sorted(lines[start:end_idx+1])
        return sorted_set[0] + sorted_set[-1]
    else:
        return None

print(solvePart2())
