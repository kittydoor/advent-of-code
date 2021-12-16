import unittest
import sys

def process(data: list[str], version: int) -> int:
    """
    Find the number of times the depth measurements increases,
    compared to the immediate previous measurement.
    """
    if version == 1:
        return part_one(data)

    if version == 2:
        return part_two(data)


# TODO: add least add a comment here to say what it does oh my god
# Love you Kate <3 Just do what you like
def part_one(report):
    size = len(report[0])
    slots = [0 for _ in range(size)]
    for r in report:
        slots = list(map(sum, zip(slots, [int(x) for x in list(r)])))

    def gamma(i):
        if i > len(report) / 2:
            return 1
        else:
            return 0

    gamma = int(''.join(map(str, (map(gamma, slots)))), 2)
    # ~gamma does not work, because it treats it as a signed int,
    # thus ~ = - n - 1, not a full invert
    epsilon = int(format(gamma, f"0>{size}b").replace('0', 'a').replace('1', '0').replace('a', '1'), 2)
    # print(f"Gamma: {gamma:0=5b} Epsilon: {epsilon:0=5b}")
    return gamma * epsilon


def part_two(report):
    pass


TEST_DATA = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(process(TEST_DATA, 1), int('10110', 2) * int('01001', 2))

    def test_two(self):
        pass
        #self.assertEqual(process(TEST_DATA, 2), -1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"usage: {{ sys.argv[0] }} <target> <version>")
        exit(1)

    target = sys.argv[1]
    version = int(sys.argv[2])
    
    with open(target) as f:
        contents = f.readlines()

    data_by_line = [line.strip() for line in contents]

    result = process(data_by_line, version)

    print(result)
