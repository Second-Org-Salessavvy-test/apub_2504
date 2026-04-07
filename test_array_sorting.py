#!/usr/bin/env python3
"""
Unit tests for array sorting module.
"""

import unittest
from array_sorting import bubble_sort, quick_sort, merge_sort, sort_array


class TestArraySorting(unittest.TestCase):
    """Test cases for array sorting functions."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
            ([3, 3, 3, 3], [3, 3, 3, 3]),
            ([-5, 10, -2, 0, 7], [-5, -2, 0, 7, 10]),
            ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90])
        ]

    def test_bubble_sort(self):
        """Test bubble sort algorithm."""
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr):
                self.assertEqual(bubble_sort(input_arr), expected)

    def test_quick_sort(self):
        """Test quick sort algorithm."""
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr):
                self.assertEqual(quick_sort(input_arr), expected)

    def test_merge_sort(self):
        """Test merge sort algorithm."""
        for input_arr, expected in self.test_cases:
            with self.subTest(input=input_arr):
                self.assertEqual(merge_sort(input_arr), expected)

    def test_sort_array_with_different_algorithms(self):
        """Test sort_array function with different algorithms."""
        test_arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]

        self.assertEqual(sort_array(test_arr, 'bubble'), expected)
        self.assertEqual(sort_array(test_arr, 'quick'), expected)
        self.assertEqual(sort_array(test_arr, 'merge'), expected)
        self.assertEqual(sort_array(test_arr, 'builtin'), expected)

    def test_sort_array_invalid_algorithm(self):
        """Test sort_array with invalid algorithm."""
        with self.assertRaises(ValueError):
            sort_array([1, 2, 3], 'invalid_algo')

    def test_original_array_unchanged(self):
        """Test that original arrays are not modified."""
        original = [5, 2, 8, 1, 9]
        original_copy = original.copy()

        bubble_sort(original)
        self.assertEqual(original, original_copy)


if __name__ == '__main__':
    unittest.main()
