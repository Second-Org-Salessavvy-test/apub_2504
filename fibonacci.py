"""
Fibonacci Series Generator
Prints the first 10 terms of the Fibonacci series
"""

def print_fibonacci(n):
    """
    Print Fibonacci series up to n terms

    Args:
        n: Number of terms to print
    """
    # First two terms
    a, b = 0, 1

    print(f"Fibonacci Series (First {n} terms):")
    print("-" * 40)

    for i in range(n):
        print(f"Term {i + 1}: {a}")
        # Update values for next iteration
        a, b = b, a + b

if __name__ == "__main__":
    # Print first 10 terms of Fibonacci series
    print_fibonacci(10)
