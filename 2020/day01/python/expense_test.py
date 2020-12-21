import unittest

from expense import calculate


class TestExpenseMethod(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(calculate([], 2), None)

    def test_single(self):
        self.assertEqual(calculate([1], 2), None)

    def test_two_2020(self):
        self.assertEqual(calculate([1000, 1020], 2), 1000 * 1020)
        self.assertEqual(calculate([800, 1220], 2), 800 * 1220)

    def test_two_not_2020(self):
        self.assertEqual(calculate([1000, 1000], 2), None)

    def test_three_2020(self):
        self.assertEqual(calculate([1000, 1100, 1020], 2), 1000 * 1020)

    def test_three_self_product_2020(self):
        self.assertEqual(calculate([1010, 1000, 1100], 2), None)

    def test_negative(self):
        with self.assertRaises(ValueError):
            calculate([-1000, 3020, 500, 413, 645], 2)

    def test_p2_two(self):
        self.assertEqual(calculate([1000, 1100], 3), None)

    def test_p2_three_2020(self):
        self.assertEqual(calculate([800, 1200, 20], 3), 800 * 1200 * 20)


if __name__ == '__main__':
    unittest.main()
