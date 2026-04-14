#!/usr/bin/env python3
"""
Fibonacci Series Generator
Prints the Fibonacci series up to the 10th term.
"""

def fibonacci(n):
    """
    Generate and print Fibonacci series up to n terms.

    Args:
        n: Number of terms to generate
    """
    a, b = 0, 1
    count = 0

    print(f"Fibonacci series up to {n} terms:")

    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

    print()  # New line at the end

if __name__ == "__main__":
    # Print Fibonacci series till 10th term
    fibonacci(10)
