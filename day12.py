example = list(map(lambda l: l.strip(), open('day12-example.txt')))
lines = list(map(lambda l: l.strip(), open('day12-input.txt')))

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

def getCurrentShip(ship_hist):
    curr_ship = ship_hist[-1]
    return [curr_ship['pos'], curr_ship['facing']]

def moveItem(curr_pos, direction, steps):
    new_pos = [] + curr_pos
    if direction == 'N':
        new_pos[1] = new_pos[1] + steps
    elif direction == 'S':
        new_pos[1] = new_pos[1] - steps
    elif direction =='E':
        new_pos[0] = new_pos[0] + steps
    elif direction =='W':
        new_pos[0] = new_pos[0] - steps
    return new_pos

directions = ['N', 'E', 'S', 'W']

def rotate(facing, degree):
    curr_dir = directions.index(facing)
    new_dir_idx = (curr_dir + (degree // 90)) % len(directions)
    return directions[new_dir_idx]

def solvePart1(moves):
    ship_hist = [{ 'pos': [0, 0], 'facing': 'E' }]
    for move in moves:
        curr_pos, facing = getCurrentShip(ship_hist)
        new_pos = [] + curr_pos
        new_facing = facing
        action = move[0]
        amt = int(move[1:])
        if action =='L':
            facing = rotate(facing, 360-amt)
        elif action =='R':
            facing = rotate(facing, amt)
        elif action =='F':
            new_pos = moveItem(curr_pos, facing, amt)
        else:
            new_pos = moveItem(curr_pos, action, amt)
        ship_hist.append({ 'pos': new_pos, 'facing': facing })
    # print(ship_hist)
    # calculate mahattan distance
    end_pos, facing = getCurrentShip(ship_hist)
    return abs(end_pos[0]) + abs(end_pos[1])

print(solvePart1(example))
print(solvePart1(lines))

def rotateWaypoint(waypoint, direction, amt):
    x_d = waypoint[0]
    y_d = waypoint[1]
    timesToRotate = amt//90
    print('times to rotate', timesToRotate)
    for i in range(timesToRotate):
        temp = x_d
        if direction == 'R':
            x_d = y_d
            y_d = -temp
        else:
            x_d = -y_d
            y_d = temp
    return [x_d, y_d]

def moveShipByWaypoint(ship, waypoint, amt):
    new_pos = [] + ship
    for i in range(amt):
        new_pos = [new_pos[0] + waypoint[0], new_pos[1] + waypoint[1]]
    return new_pos

def solvePart2(moves):
    history = [{ 'ship': [0, 0], 'waypoint': [10, 1] }]
    print(moves)
    for move in moves:
        curr_state = history[-1]
        curr_ship = curr_state['ship']
        curr_waypoint = curr_state['waypoint']
        new_ship = [] + curr_ship
        new_waypoint = [] + curr_waypoint
        action = move[0]
        amt = int(move[1:])
        if action =='L':
            new_waypoint = rotateWaypoint(curr_waypoint, 'L', amt)
        elif action =='R':
            new_waypoint = rotateWaypoint(curr_waypoint, 'R', amt)
        elif action =='F':
            new_ship = moveShipByWaypoint(curr_ship, curr_waypoint, amt)
        else:
            new_waypoint = moveItem(curr_waypoint, action, amt)
        history.append({ 'ship': new_ship, 'waypoint': new_waypoint })
    # print(history)
    # calculate mahattan distance
    final_ship_pos = history[-1]['ship']
    return abs(final_ship_pos[0]) + abs(final_ship_pos[1])

print(solvePart2(example))
print(solvePart2(lines))
