boarding_passes = open('day5-input.txt', 'r').readlines()

# Find the row and column
# return row * 8 + column

# first 7 characters is front - back (128 rows)
# last 3 is left - right (8 columns)
def find_row(boarding_pass):
    rows = range(0, 128)

    for char in boarding_pass:
        middle = int(len(rows)/2)
        if char == 'F':
            rows = rows[0:middle]
        else:
            rows = rows[middle:]

    return rows[0]

def find_column(boarding_pass):
    rows = range(0, 8)

    for char in boarding_pass:
        middle = int(len(rows)/2)
        if char == 'L':
            rows = rows[0:middle]
        else:
            rows = rows[middle:]

    return rows[0]

def findSeatId(boarding_pass):
    row = find_row(boarding_pass[0:7])
    column = find_column(boarding_pass[7:])
    # print(boarding_pass[0:7])
    # print(boarding_pass[7:])
    # print(row, column)
    return row * 8 + column

def findSeat():
    highest_id = 0
    for boarding_pass in boarding_passes:
        seat_id = findSeatId(boarding_pass)
        if seat_id > highest_id:
            highest_id = seat_id
    return highest_id


print('BFFFBBFRRR', findSeatId('BFFFBBFRRR'))
print('FFFBBBFRRR', findSeatId('FFFBBBFRRR'))
print('BBFFBBFRLL', findSeatId('BBFFBBFRLL'))

# print('FFFFFFF', find_row('FFFFFFF'))
# print('BBBBBBB', find_row('BBBBBBB'))
# print('RLL', find_column('RLL'))
# print('RRR', find_column('RRR'))
print(findSeat())

# no seats at the front OR back (where row = 0 or row = 127)
# every other seat will be filled, and the seats with IDs +1 and -1 from my seat are on the list
# your seat is the only one missing
# seats from the front row will have IDs: 0 * 8 + column so that doesn't make sense
# seats from the back will have IDs: 127 * 8 + column
# max seat ID is 1015 (inclusive)
# min seat ID is 8 (inclusive)
def findMissingSeats():
    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_id = findSeatId(boarding_pass)
        seat_ids.append(seat_id)

    sorted_seats = sorted(seat_ids)
    for i in range(len(sorted_seats)):
        if sorted_seats[i + 1] - sorted_seats[i] > 1:
            return sorted_seats[i] + 1

print(findMissingSeats())
