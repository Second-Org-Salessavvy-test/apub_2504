#!/usr/bin/env python3
"""
Fibonacci Series Generator
Prints the first 10 terms of the Fibonacci sequence.
"""


def print_fibonacci(n):
    """
    Print the first n terms of the Fibonacci series.

    Args:
        n (int): Number of terms to print
    """
    # Initialize the first two terms
    first = 0
    second = 1

    print(f"Fibonacci Series (first {n} terms):")

    # Print the series
    for i in range(n):
        if i == 0:
            # First term
            print(first, end=" ")
        elif i == 1:
            # Second term
            print(second, end=" ")
        else:
            # Calculate next term as sum of previous two
            next_term = first + second
            print(next_term, end=" ")
            # Update for next iteration
            first = second
            second = next_term

    print()  # New line at the end


if __name__ == "__main__":
    # Print first 10 terms of Fibonacci series
    print_fibonacci(10)
