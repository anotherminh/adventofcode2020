import string
import re

passportFile = open('day4-input.txt', 'r').readlines()

def is_hex(s):
     hex_digits = set(string.hexdigits)
     return all(c in hex_digits for c in s)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def valid_entry(key, val):
    if key == 'byr':
        return len(val) == 4 and int(val) in range(1920, 2003)
    elif key == 'iyr':
        return len(val) == 4 and int(val) in range(2010, 2021)
    elif key == 'eyr':
        return len(val) == 4 and int(val) in range(2020, 2031)
    elif key == 'hgt':
        unit = val[-2:]
        h = val[:-2]
        if (unit == 'cm'):
            return int(h) in range(150, 194)
        elif (unit == 'in'):
            return int(h) in range(59, 77)
        else:
            return False
    elif key == 'hcl':
        return val[0] == '#' and is_hex(val[1:]) and len(val[1:]) == 6
    elif key == 'ecl':
        return val in valid_eye_colors
    elif key == 'pid':
        return len(val) == 9 and val.isnumeric()
    elif key == 'cid':
        return True
    else:
        False


def countValidPassports(validate_entry = True):
    valid = 0
    seen_fields = set()

    for line in passportFile:
        entries = line.split()
        # empty line, check to see if passport is valid
        if len(entries) == 0:
            isValid = all(field in seen_fields for field in required_fields)
            if isValid:
                valid += 1

            seen_fields = set()
        else:
            for entry in entries:
                key, val = entry.split(':')
                if (not validate_entry) or valid_entry(key, val):
                    seen_fields.add(key)

    return valid

print(countValidPassports(False))
print(countValidPassports())
