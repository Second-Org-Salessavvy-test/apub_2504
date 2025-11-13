#!/usr/bin/env python3

import unittest
from reverse_string import reverse_string


class TestReverseString(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_string_with_numbers(self):
        self.assertEqual(reverse_string("abc123"), "321cba")

    def test_string_with_special_chars(self):
        self.assertEqual(reverse_string("hello!@#"), "#@!olleh")


if __name__ == "__main__":
    unittest.main()
