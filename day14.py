import re
lines = open('day14-input.txt').readlines()

def applyBitmask(mask, value):
    binary = format(value, '#038b')
    masked = '0b'
    for i in range(len(mask)):
        if mask[i] == 'X':
            # + 2 because of the leading 0b characters
            masked += binary[i + 2]
        else:
            masked += mask[i]
    return int(masked, 2)

# applyBitmask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11)
# applyBitmask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101)
# applyBitmask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0)

def solve1(program):
    mem = {}
    mask = None
    for ins in program:
        if ins.startswith('mask'):
            _, mask = ins.split('=')
            mask = mask.strip()
        elif ins.startswith('mem'):
            register, value = ins.split('=')
            register = int(re.findall('\[\d+\]', register)[0][1:-1])
            value = int(value)
            #write to memory
            mem[register] = applyBitmask(mask, value)
    total = 0
    for k in mem:
        total += mem[k]
    return total

print(solve1(lines))

def applyBitmaskToAddr(mask, addr):
    addrs = ['']
    binary = format(addr, '#038b')
    masked = '0b'
    for i in range(len(mask)):
        if mask[i] == 'X':
            with_zeros = []
            with_ones = []
            for a in addrs:
                with_zeros.append(a + '0')
            for a in addrs:
                with_ones.append(a + '1')
            addrs = with_zeros + with_ones
        elif mask[i] == '1':
            addrs = [a + '1' for a in addrs]
        else:
            addrs = [a + binary[i + 2] for a in addrs]
    return [int(a, 2) for a in addrs]

applyBitmaskToAddr('000000000000000000000000000000X1001X', 42)

def solve2(program):
    mem = {}
    mask = None
    for ins in program:
        if ins.startswith('mask'):
            _, mask = ins.split('=')
            mask = mask.strip()
        elif ins.startswith('mem'):
            register, value = ins.split('=')
            register = int(re.findall('\[\d+\]', register)[0][1:-1])
            value = int(value)
            addrs = applyBitmaskToAddr(mask, register)
            #write to memory
            for addr in addrs:
                mem[addr] = value
    total = 0
    for k in mem:
        total += mem[k]
    return total

print(solve2(lines))
