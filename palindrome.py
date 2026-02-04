def is_palindrome(text):
    """
    Check if a string is a palindrome.

    Args:
        text (str): The string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned = text.replace(" ", "").lower()

    # Compare the string with its reverse
    return cleaned == cleaned[::-1]


def is_palindrome_number(num):
    """
    Check if a number is a palindrome.

    Args:
        num (int): The number to check

    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Convert to string and check if it reads the same forwards and backwards
    num_str = str(num)
    return num_str == num_str[::-1]


# Example usage
if __name__ == "__main__":
    # Test with strings
    test_strings = ["racecar", "hello", "A man a plan a canal Panama", "python"]

    print("String palindrome tests:")
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' is {'a palindrome' if result else 'not a palindrome'}")

    print("\nNumber palindrome tests:")
    # Test with numbers
    test_numbers = [121, 123, 12321, 1000]

    for n in test_numbers:
        result = is_palindrome_number(n)
        print(f"{n} is {'a palindrome' if result else 'not a palindrome'}")
