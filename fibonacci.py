def fibonacci(n):
    """Print Fibonacci series up to n terms."""
    a, b = 0, 1
    count = 0

    print(f"Fibonacci series up to {n} terms:")
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()

if __name__ == "__main__":
    fibonacci(10)
