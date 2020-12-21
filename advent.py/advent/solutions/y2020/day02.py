"""Toboggan Password Verification Application
"""
import sys
from collections import Counter


def verify(password, char, min_count, max_count):
    """Return whether a password passes given criteria of
    within the password there should be at least min_count
    and at most max_count occurrences of char.

    >>> verify('password', 'a', 1, 3)
    True

    >>> verify('password', 'b', 2, 4)
    False
    """
    if password == '':
        return None

    if ' ' in password:
        raise ValueError("No spaces are allowed in a password")

    if len(char) > 1:
        raise ValueError("Value of char should be a single character")

    if char == '' and (min_count != 0 or max_count != 0):
        raise ValueError("Rule has counts, but no char defined")

    if char == '' and min_count == 0 and max_count == 0:
        return None

    if min_count <= Counter(password)[char] <= max_count:
        return True
    return False


def parse(line):
    """Given a line containing password and criteria,
    parse it and break it into components

    >>> parse('1-3 a: password')
    ('password', 'a', 1, 3)

    >>> parse('2-4 c: supersecure')
    ('supersecure', 'c', 2, 4)
    """
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

    min_count, max_count = counts.split('-')
    min_count = int(min_count)
    max_count = int(max_count)

    return (password, char, min_count, max_count)


def process(line):
    """Combine parse and verify to test a line containing
    a password and criteria

    >>> process('1-3 a: password')
    True

    >>> process('2-4 c: supersecure')
    False
    """
    result = parse(line)
    if not result:
        return None

    password, char, min_count, max_count = result
    return verify(password, char, min_count, max_count)


def main():
    """Count all passwords in given file that match their respective rules
    """
    if len(sys.argv) < 2:
        print("usage: toboggan.py <db>")
        sys.exit(1)

    db_file = sys.argv[1]

    with open(db_file) as f:
        contents = f.readlines()

    database = [line.strip() for line in contents]

    valid_passwords = 0
    for row in database:
        if process(row):
            valid_passwords += 1

    print(valid_passwords)


if __name__ == '__main__':
    main()
