"""Test module for toboggan"""
import unittest

from .day02 import parse, process, verify

invalid_values = [
    "1-3 : abcde",
    "1- : abcde",
    "-3 : abcde",
    "1- a: abcde",
    "-3 a: abcde",
    "1 a: abcde",
    "abcde",
    ": abcde",
    ":abcde",
    "a: abcde",
]


class TestProcessMethod(unittest.TestCase):
    """Test functionality of the process func"""

    def test_empty(self):
        """Test for empty input"""
        self.assertEqual(process(""), None)

    def test_valid(self):
        """Test for some sample valid inputs"""
        valid_results = [
            ("1-3 a: abcde", True),
            ("1-3 b: cdefg", False),
            ("2-9 c: ccccccccc", True),
        ]

        for line, result in valid_results:
            with self.subTest(line=line, result=result):
                self.assertEqual(process(line), result)

    def test_invalid(self):
        """Test for some sample invalid inputs"""
        for val in invalid_values:
            with self.subTest(val=val):
                with self.assertRaises(ValueError):
                    process(val)


class TestParseMethod(unittest.TestCase):
    """Test functionality of the parse func"""

    def test_empty(self):
        """Test for empty input"""
        self.assertEqual(parse(""), None)

    def test_valid_rule(self):
        """Test for valid input"""
        self.assertEqual(parse("1-3 a: abcde"), ("abcde", 'a', 1, 3))

    def test_invalid_rules(self):
        """ Test for invalid input"""
        for val in invalid_values:
            with self.subTest(val=val):
                with self.assertRaises(ValueError):
                    parse(val)


class TestVerifyMethod(unittest.TestCase):
    """Test functionality of the verify func"""
    def test_empty(self):
        """Test for completely empty input"""
        self.assertEqual(verify("", "", 0, 0), None)

    def test_empty_pass_no_char(self):
        """Test for only counts"""
        self.assertEqual(verify("", "", 1, 3), None)

    def test_empty_pass(self):
        """Test for complete except for password input"""
        self.assertEqual(verify("", "a", 1, 3), None)

    def test_empty_char_no_count(self):
        """Test for no char or no count input"""
        self.assertEqual(verify("pass", "", 0, 0), None)

    def test_no_space_in_password(self):
        """Test for password with space input"""
        with self.assertRaises(ValueError):
            verify("ab de", "a", 1, 3)

    def test_empty_char_with_count(self):
        """Test for password with count but no char input"""
        with self.assertRaises(ValueError):
            verify("pass", "", 1, 3)

    def test_not_a_char(self):
        """Test for invalid char input"""
        with self.assertRaises(ValueError):
            verify("pass", "abc", 1, 3)

    def test_valid_password_count_one(self):
        """Test for valid password with 1-1 bounds"""
        self.assertEqual(verify("abc", "a", 1, 1), True)

    def test_valid_password_count_different(self):
        """Test for valid password with different bounds"""
        self.assertEqual(verify("abc", "a", 1, 3), True)

    def test_valid_password_count_large(self):
        """Test for valid password with larger than 1 bounds"""
        self.assertEqual(verify("abc", "a", 2, 3), False)

    def test_examples(self):
        """Test given examples"""
        self.assertEqual(verify("abcde", "a", 1, 3), True)
        self.assertEqual(verify("cdefg", "b", 1, 3), False)
        self.assertEqual(verify("ccccccccc", "c", 2, 9), True)


if __name__ == "__main__":
    unittest.main()
