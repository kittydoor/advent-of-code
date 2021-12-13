import unittest
import sys

def process(data: list[str], version: int) -> int:
    """
    Find the number of times the depth measurements increases,
    compared to the immediate previous measurement.
    """
    measurements = [int(d) for d in data]

    if version == 1:
        return part_one(measurements)

    if version == 2:
        return part_two(measurements)


def part_one(measurements):
    count = 0

    m_iter = iter(measurements)
    last_m = next(m_iter)
    for m in m_iter:
        if m > last_m:
            count = count + 1
        last_m = m

    return count


def part_two(measurements):
    count = 0

    m_iter = iter(measurements)
    i = 0
    j = next(m_iter)
    k = next(m_iter)
    l = next(m_iter)

    for m in m_iter:
        i = j
        j = k
        k = l
        l = m
        if j + k + l > i + j + k:
            count = count + 1

    return count


TEST_DATA = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(process(TEST_DATA, 1), 7)

    def test_two(self):
        self.assertEqual(process(TEST_DATA, 2), 5)


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
