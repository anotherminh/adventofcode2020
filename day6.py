answers = open('day6-input.txt').readlines()

def count_yes_answers():
    sum_of_yes = 0
    group_count = 0
    group_answers = {}

    for line in answers:
        chars = line.strip()
        if (len(chars)) == 0:
            for k in group_answers:
                if group_answers[k] == group_count:
                    sum_of_yes += 1
            group_answers = {}
            group_count = 0
        else:
            group_count += 1
            for c in chars:
                if c in group_answers:
                    group_answers[c] += 1
                else:
                    group_answers[c] = 1
    return sum_of_yes


# 377724 is too high, forgot to reset the group count
# 1621 is too low, was counting the wrong thing
# 7113 is too high, was counting \n (should always trim them!)
print(count_yes_answers())
