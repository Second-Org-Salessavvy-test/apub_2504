#!/usr/bin/env python3
"""
Simple array sorting utility.

This module provides functions to sort arrays using various algorithms.
"""


def sort_array(arr):
    """
    Sort an array in ascending order.

    Args:
        arr: List of comparable elements to sort

    Returns:
        Sorted list in ascending order
    """
    return sorted(arr)


def sort_array_descending(arr):
    """
    Sort an array in descending order.

    Args:
        arr: List of comparable elements to sort

    Returns:
        Sorted list in descending order
    """
    return sorted(arr, reverse=True)


def main():
    """Example usage of array sorting functions."""
    # Example arrays
    numbers = [64, 34, 25, 12, 22, 11, 90]
    strings = ["banana", "apple", "cherry", "date"]

    print("Original array:", numbers)
    print("Sorted ascending:", sort_array(numbers))
    print("Sorted descending:", sort_array_descending(numbers))
    print()
    print("Original strings:", strings)
    print("Sorted strings:", sort_array(strings))


if __name__ == "__main__":
    main()
