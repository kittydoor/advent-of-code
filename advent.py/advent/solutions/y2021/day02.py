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


def part_one(cmds):
    horizon = 0
    depth = 0

    for cmd in cmds:
        direction, count = cmd.split(' ')
        count = int(count)

        if direction == 'forward':
            horizon = horizon + count
        elif direction == 'backward':
            horizon = horizon - count
        elif direction == 'up':
            depth = depth - count
        elif direction == 'down':
            depth = depth + count
        else:
            print("This should not happen")

    return horizon * depth


def part_two(cmds):
    pass


TEST_DATA = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(process(TEST_DATA, 1), 15*10)

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
