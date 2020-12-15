starting_numbers = [2,0,1,9,5,19]

example1 = [1,3,2] # 1
example2 = [2,1,3] # 10
example3 = [1,2,3] # 27

def solve1(start_numbers, stop_at):
    spoken_nums = {}
    for idx in range(len(start_numbers)):
        spoken_nums[start_numbers[idx]] = [idx]
    last_spoken_num = start_numbers[-1]
    turn = len(spoken_nums)
    while turn < stop_at:
        if last_spoken_num in spoken_nums:
            first_spoken = len(spoken_nums[last_spoken_num]) <= 1
            if first_spoken:
                current_spoken = 0
            else:
                prev_spoken = spoken_nums[last_spoken_num]
                current_spoken = prev_spoken[-1] - prev_spoken[-2]
        if current_spoken in spoken_nums:
            spoken_nums[current_spoken].append(turn)
            spoken_nums[current_spoken] = spoken_nums[current_spoken][-2:]
        else:
            spoken_nums[current_spoken] = [turn]
        turn += 1
        last_spoken_num = current_spoken
    print(last_spoken_num)
    return last_spoken_num

# solve1(example1, 2020)
# solve1(example2, 2020)
# solve1(example3, 2020)
# solve1(starting_numbers, 2020)
solve1([3,2,1], 100)

# I don't have a faster solution...
# solve1(starting_numbers, 30_000_000)
