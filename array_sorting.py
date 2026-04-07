#!/usr/bin/env python3
"""
Array Sorting Implementation

This module provides various sorting algorithms for arrays.
"""


def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break

    return arr_copy


def quick_sort(arr):
    """
    Sort an array using quick sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n)
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """
    Sort an array using merge sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort_array(arr, algorithm='quick'):
    """
    Sort an array using the specified algorithm.

    Args:
        arr: List of comparable elements
        algorithm: Sorting algorithm to use ('bubble', 'quick', 'merge', 'builtin')

    Returns:
        Sorted list in ascending order

    Raises:
        ValueError: If invalid algorithm is specified
    """
    if not arr:
        return []

    algorithms = {
        'bubble': bubble_sort,
        'quick': quick_sort,
        'merge': merge_sort,
        'builtin': lambda x: sorted(x)
    }

    if algorithm not in algorithms:
        raise ValueError(f"Invalid algorithm. Choose from: {', '.join(algorithms.keys())}")

    return algorithms[algorithm](arr)


def main():
    """Demonstration of array sorting."""
    # Example arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [-5, 10, -2, 0, 7]
    ]

    print("Array Sorting Demonstration")
    print("=" * 50)

    for arr in test_arrays:
        print(f"\nOriginal array: {arr}")
        print(f"Bubble sort:    {sort_array(arr, 'bubble')}")
        print(f"Quick sort:     {sort_array(arr, 'quick')}")
        print(f"Merge sort:     {sort_array(arr, 'merge')}")


if __name__ == "__main__":
    main()
