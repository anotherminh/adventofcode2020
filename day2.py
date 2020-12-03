passwordFile = open('day2-input.txt', 'r')
passwords = list(map(lambda x: x.split(), passwordFile.readlines()))

def countValidPasswords():
    validCount = 0
    for count, letter, password in passwords:
        [min_count, max_count] = list(map(int, count.split('-')))
        letter = letter[0]
        letterCount = password.count(letter)
        if letterCount in range(min_count, max_count + 1):
            validCount += 1
    return validCount

print(countValidPasswords())

def countOtherValidPasswords():
    validCount = 0
    for count, letter, password in passwords:
        [pos1, pos2] = list(map(int, count.split('-')))
        letter = letter[0]
        idx1 = pos1 - 1
        idx2 = pos2 - 1
        if (password[idx1] == letter) ^ (password[idx2] == letter):
            validCount += 1
    return validCount

print(countOtherValidPasswords())
