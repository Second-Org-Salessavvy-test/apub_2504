"""
Fibonacci Series Generator
This script prints the Fibonacci series up to 10 terms.
"""

def print_fibonacci(n):
    """
    Print Fibonacci series up to n terms.

    Args:
        n (int): Number of terms to print
    """
    # First two terms
    a, b = 0, 1
    count = 0

    print(f"Fibonacci Series up to {n} terms:")

    # Check if n is valid
    if n <= 0:
        print("Please enter a positive integer")
        return
    elif n == 1:
        print(a)
        return

    # Print Fibonacci series
    while count < n:
        print(a, end=" ")
        # Update values
        a, b = b, a + b
        count += 1
    print()  # New line after series

if __name__ == "__main__":
    # Print Fibonacci series up to 10 terms
    print_fibonacci(10)
