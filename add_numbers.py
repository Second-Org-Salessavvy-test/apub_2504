def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"{num1} + {num2} = {result}")

    # Interactive input
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print(f"Sum: {add_numbers(x, y)}")
    except ValueError:
        print("Please enter valid numbers")
