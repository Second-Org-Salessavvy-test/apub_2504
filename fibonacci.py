#!/usr/bin/env python3
"""
Fibonacci Series Generator
Prints the Fibonacci series up to 10 terms
"""

def fibonacci_series(n):
    """
    Generate and print Fibonacci series up to n terms

    Args:
        n (int): Number of terms to generate
    """
    # First two terms
    a, b = 0, 1
    count = 0

    print(f"Fibonacci Series up to {n} terms:")

    # Generate Fibonacci series
    while count < n:
        print(a, end=" ")
        # Update values
        a, b = b, a + b
        count += 1
    print()  # New line at the end

if __name__ == "__main__":
    # Print Fibonacci series up to 10 terms
    fibonacci_series(10)
