instructions = open('day8-input.txt').readlines()
# instructions = open('day8-example.txt').readlines()

def brokenAcc():
    instructions_ran = set()
    acc = 0
    idx = 0
    while idx in range(len(instructions)):
        if idx in instructions_ran:
            return acc
        else:
            ins = instructions[idx]
            instructions_ran.add(idx)
            op, num = ins.split(' ')
            if op == 'acc':
                acc += int(num)
                idx += 1
            elif op == 'jmp':
                idx += int(num)
            else:
                idx += 1
    return 'Should never get here'

print(brokenAcc())

# Fix the program by changing exactly one jmp to nop or nop to jmp
# Find all the fixable instructions, and fix them to see if the program terminates

# returns the acc if it reaches the end, else NONE
def acc(modified_instructions):
    instructions_ran = []
    acc = 0
    idx = 0
    while idx in range(len(modified_instructions)):
        if idx in instructions_ran:
            return None
        else:
            ins = modified_instructions[idx]
            instructions_ran.append(idx)
            op, num = ins.split(' ')
            if op == 'acc':
                acc += int(num)
                idx += 1
            elif op == 'jmp':
                idx += int(num)
            else:
                idx += 1

    if idx == len(instructions):
        return acc
    else:
        return None

def findFixableLines():
    fixable = []
    for idx in range(len(instructions)):
        op, num = instructions[idx].split(' ')
        # if idx == len(instructions) - 1 and op not
        if op != 'acc':
            fixable.append(idx)
    return fixable

def fixProgram():
    candidates = findFixableLines()
    for idx in candidates:
        op, num = instructions[idx].split(' ')
        new_op = None
        if op == 'jmp':
            new_op = 'nop'
        else:
            new_op = 'jmp'
        modified_inst = instructions[0:idx]
        modified_inst.append(new_op + ' ' + num)
        modified_inst += instructions[(idx+1):]
        res = acc(modified_inst)
        if res != None:
            return res

    return 'Found nothing'

print(fixProgram())

