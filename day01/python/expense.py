import sys
import itertools
from functools import reduce

def calculate(values: list[int], count: int) -> int:
    """
    Find the two pairs that add up to 2020 in a list of numbers,
    return their product.
    """
    if len(values) < count:
        return None

    for i in values:
        if i < 0:
            raise ValueError("Expense report contains negative number")

    for combination in itertools.combinations(values, count):
        if sum(combination) == 2020:
            return reduce((lambda x, y: x * y), combination)

    # final resort
    return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("usage: expense.py <target> <count>")
        exit(1)

    target = sys.argv[1]
    count = int(sys.argv[2])

    with open(target) as f:
        contents = f.readlines()

    expense_report = [ int(line.strip()) for line in contents ]

    result = calculate(expense_report, count)

    print(result)
