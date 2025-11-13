import unittest
from utils.string_utils import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverse_simple_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_string_with_special_characters(self):
        self.assertEqual(reverse_string("hello!@#"), "#@!olleh")

    def test_reverse_string_with_numbers(self):
        self.assertEqual(reverse_string("abc123"), "321cba")

    def test_reverse_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_reverse_unicode_string(self):
        self.assertEqual(reverse_string("🎉🎊🎈"), "🎈🎊🎉")

    def test_reverse_string_with_newlines(self):
        self.assertEqual(reverse_string("hello\nworld"), "dlrow\nolleh")

    def test_type_error_with_integer(self):
        with self.assertRaises(TypeError):
            reverse_string(123)

    def test_type_error_with_list(self):
        with self.assertRaises(TypeError):
            reverse_string(["hello"])

    def test_type_error_with_none(self):
        with self.assertRaises(TypeError):
            reverse_string(None)


if __name__ == "__main__":
    unittest.main()
