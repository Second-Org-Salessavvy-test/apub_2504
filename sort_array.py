"""
Array Sorting Program

This module provides functions to sort arrays using different algorithms.
"""


def bubble_sort(arr):
    """Sort an array using bubble sort algorithm."""
    n = len(arr)
    result = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def quick_sort(arr):
    """Sort an array using quick sort algorithm."""
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Sort an array using merge sort algorithm."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted arrays into one sorted array."""
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


def main():
    """Demonstrate the sorting algorithms."""
    sample_array = [64, 34, 25, 12, 22, 11, 90]

    print(f"Original array: {sample_array}")
    print(f"Bubble sort:    {bubble_sort(sample_array)}")
    print(f"Quick sort:     {quick_sort(sample_array)}")
    print(f"Merge sort:     {merge_sort(sample_array)}")


if __name__ == "__main__":
    main()
