import itertools

def calculate(values: list[int]) -> int:
    """
    Find the two pairs that add up to 2020 in a list of numbers,
    return their product.
    """
    if len(values) < 2:
        return None

    for i in values:
        if i < 0:
            raise ValueError("Expense report contains negative number")

    for first, second in itertools.combinations(values, 2):
        if first + second == 2020:
            return first * second

    # final resort
    return None

if __name__ == '__main__':
    with open("../input.txt") as f:
        contents = f.readlines()

    expense_report = [ int(line.strip()) for line in contents ]

    result = calculate(expense_report)

    print(result)
