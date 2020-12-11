import copy

def chars(word):
    return [char for char in word]

lines = list(map(lambda x: chars(x.strip()), open('day11-input.txt').readlines()))
# lines = list(map(lambda x: chars(x.strip()), open('day11-example.txt').readlines()))

deltas = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def count_neighbors(idx, state):
    count = 0
    for i, j in deltas:
        neighbor_i = i + idx[0]
        neighbor_j = j + idx[1]
        if neighbor_i in range(0, len(state)) and neighbor_j in range(0, len(state[0])):
            neighbor = state[neighbor_i][neighbor_j]
            if neighbor == '#':
                count += 1
    return count

def pretty_print(state):
    new_state = ''
    for l in state:
        row = ''
        for cell in l:
            row += cell
        row += '\n'
        new_state += row
    print(new_state)

def state_changed(curr_state, next_state):
    for idx in range(len(curr_state)):
        if next_state[idx] != curr_state[idx]:
            return True
    return False

def count_all_occupied(state):
    count = 0
    for line in state:
        for cell in line:
            if cell == '#':
                count += 1
    return count

def solvePart1(state, stop_at):
    solved = False
    round_count = 0
    curr_state = state
    next_state = copy.deepcopy(curr_state)
    while not solved and round_count < stop_at:
        # pretty_print(curr_state)
        for i in range(len(curr_state)):
            for j in range(len(curr_state[i])):
                if lines[i][j] != '.':
                    occupied_neighbors = count_neighbors([i, j], curr_state)
                    if occupied_neighbors == 0 and curr_state[i][j] == 'L':
                        next_state[i][j] = '#'
                    elif occupied_neighbors >= 4 and curr_state[i][j] == '#':
                        next_state[i][j] = 'L'
        # pretty_print(curr_state)
        if not state_changed(next_state, curr_state):
            solved = True
        curr_state = next_state
        next_state = copy.deepcopy(curr_state)

        round_count += 1
    return count_all_occupied(next_state)

print(solvePart1(lines, 1000000))

def count_neighbors2(indices, state):
    neighbors = []
    for i_delta, j_delta in deltas:
        seat_not_found = True
        inbound = True
        length = 1
        while seat_not_found and inbound:
            n_i = indices[0] + i_delta * length
            n_j = indices[1] + j_delta * length
            if n_i in range(len(state)) and n_j in range(len(state[0])):
                if state[n_i][n_j] != '.':
                    neighbors.append(state[n_i][n_j])
                    seat_not_found = False
                else:
                    length += 1
            else:
                inbound = False
    count = 0
    for n in neighbors:
        if n == '#':
            count += 1
    return count

def solvePart2(state, stop_at):
    solved = False
    round_count = 0
    curr_state = state
    next_state = copy.deepcopy(curr_state)
    while not solved and round_count < stop_at:
        # pretty_print(curr_state)
        for i in range(len(curr_state)):
            for j in range(len(curr_state[i])):
                if lines[i][j] != '.':
                    occupied_neighbors = count_neighbors2([i, j], curr_state)
                    if occupied_neighbors == 0 and curr_state[i][j] == 'L':
                        next_state[i][j] = '#'
                    elif occupied_neighbors >= 5 and curr_state[i][j] == '#':
                        next_state[i][j] = 'L'
        # pretty_print(next_state)
        if not state_changed(next_state, curr_state):
            solved = True
        curr_state = next_state
        next_state = copy.deepcopy(curr_state)
        round_count += 1

    return count_all_occupied(next_state)

print(solvePart2(lines, 1000))
