"""
Fibonacci Series Generator
Prints the Fibonacci series up to 10 terms
"""

def print_fibonacci(n):
    """
    Print Fibonacci series up to n terms

    Args:
        n (int): Number of terms to print
    """
    # First two terms
    a, b = 0, 1
    count = 0

    # Check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
        return
    elif n == 1:
        print(f"Fibonacci series up to {n} term:")
        print(a)
        return
    else:
        print(f"Fibonacci series up to {n} terms:")
        while count < n:
            print(a, end=" ")
            # Update values
            a, b = b, a + b
            count += 1
        print()  # New line at the end

if __name__ == "__main__":
    # Print Fibonacci series up to 10 terms
    print_fibonacci(10)
