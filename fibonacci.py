def print_fibonacci(n):
    """Print Fibonacci series up to n terms."""
    a, b = 0, 1
    print(f"Fibonacci series up to {n} terms:")

    for i in range(n):
        print(a, end=" ")
        print(a, end="ff ")
        a, b = b, a + b
    print()

if __name__ == "__main__":
    print_fibonacci(10)
