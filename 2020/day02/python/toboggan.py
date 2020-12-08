import sys
from collections import Counter

def verify(password, char, min, max):
    if password == "":
        return None

    if ' ' in password:
        raise ValueError("No spaces are allowed in a password")

    if len(char) > 1:
        raise ValueError("Value of char should be a single character")
    elif char == "" and (min != 0 or max != 0):
        raise ValueError("Rule has counts, but no char defined")
    elif char == "" and min == 0 and max == 0:
        return None

    if min <= Counter(password)[char] <= max:
        return True
    return False

def parse(line):
    if not line.strip():
        return None

    if ':' not in line:
        raise ValueError("No : in db item")

    rule, password = line.split(':')
    rule = rule.strip()
    password = password.strip()

    counts, char = rule.split(' ')
    counts = counts.strip()
    char = char.strip()

    min, max = counts.split('-')
    min = int(min)
    max = int(max)

    return (password, char, min, max)

def process(line):
     result = parse(line)
     if not result:
         return None

     password, char, min, max = result
     return verify(password, char, min, max)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: toboggan.py <db>")
        exit(1)

    db_file = sys.argv[1]

    with open(db_file) as f:
        contents = f.readlines()

    db = [ line.strip() for line in contents ]

    valid_passwords = 0
    for row in db:
        if process(row):
            valid_passwords += 1

    print(valid_passwords)
