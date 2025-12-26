def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a string that reads the same forward and backward,
    ignoring case and non-alphanumeric characters.

    Args:
        s: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Compare the string with its reverse
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Example usage
    test_strings = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "hello",
        "Was it a car or a cat I saw?",
        "No lemon, no melon",
        "python"
    ]

    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")
