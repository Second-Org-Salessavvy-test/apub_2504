"""
Array Sorting Program
This program demonstrates various array sorting algorithms and techniques in Python.
"""


def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    arr_copy = arr.copy()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break

    return arr_copy


def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    arr_copy = arr.copy()
    n = len(arr_copy)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]

    return arr_copy


def insertion_sort(arr):
    """
    Sorts an array using the insertion sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    arr_copy = arr.copy()

    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key

    return arr_copy


def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.
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
    Sorts an array using the merge sort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort."""
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


def built_in_sort(arr):
    """
    Sorts an array using Python's built-in sorted() function.
    Uses Timsort algorithm (hybrid of merge sort and insertion sort).
    Time Complexity: O(n log n)
    """
    return sorted(arr)


def demonstrate_sorting():
    """Demonstrates all sorting algorithms with sample arrays."""

    # Sample arrays to sort
    arrays = {
        "Random integers": [64, 34, 25, 12, 22, 11, 90],
        "Reversed array": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "Nearly sorted": [1, 2, 3, 5, 4, 6, 7],
        "With duplicates": [5, 2, 8, 2, 9, 1, 5, 5]
    }

    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Built-in Sort": built_in_sort
    }

    for array_name, array in arrays.items():
        print(f"\n{'=' * 60}")
        print(f"Array: {array_name}")
        print(f"Original: {array}")
        print(f"{'=' * 60}")

        for algo_name, algo_func in sorting_algorithms.items():
            sorted_array = algo_func(array)
            print(f"{algo_name:20s}: {sorted_array}")


if __name__ == "__main__":
    print("Python Array Sorting Demonstration")
    print("=" * 60)

    demonstrate_sorting()

    # Interactive section
    print("\n" + "=" * 60)
    print("Custom Array Sorting")
    print("=" * 60)

    try:
        user_input = input("\nEnter numbers separated by spaces (or press Enter to skip): ")

        if user_input.strip():
            custom_array = [int(x) for x in user_input.split()]
            print(f"\nOriginal array: {custom_array}")
            print(f"Sorted array:   {built_in_sort(custom_array)}")
        else:
            print("\nNo input provided. Exiting.")

    except ValueError:
        print("\nInvalid input. Please enter only numbers separated by spaces.")
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
