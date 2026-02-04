#!/usr/bin/env python3
"""
Palindrome Checker
A utility to check if a string is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters
that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
"""


def is_palindrome(text):
    """
    Check if a given string is a palindrome.

    Args:
        text (str): The string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Compare the string with its reverse
    return cleaned_text == cleaned_text[::-1]


def is_palindrome_advanced(text, ignore_case=True, ignore_spaces=True, ignore_punctuation=True):
    """
    Advanced palindrome checker with customizable options.

    Args:
        text (str): The string to check
        ignore_case (bool): Whether to ignore case differences
        ignore_spaces (bool): Whether to ignore spaces
        ignore_punctuation (bool): Whether to ignore punctuation

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    processed_text = text

    if ignore_case:
        processed_text = processed_text.lower()

    if ignore_punctuation:
        processed_text = ''.join(char for char in processed_text if char.isalnum() or char.isspace())

    if ignore_spaces:
        processed_text = processed_text.replace(' ', '')

    return processed_text == processed_text[::-1]


def main():
    """
    Main function to demonstrate palindrome checking.
    """
    # Test cases
    test_strings = [
        "racecar",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "hello",
        "Madam",
        "12321",
        "12345"
    ]

    print("=" * 50)
    print("Palindrome Checker - Test Results")
    print("=" * 50)

    for test_str in test_strings:
        result = is_palindrome(test_str)
        print(f"\n'{test_str}'")
        print(f"Is palindrome: {result}")

    print("\n" + "=" * 50)
    print("Interactive Mode")
    print("=" * 50)

    # Interactive mode
    while True:
        user_input = input("\nEnter a string to check (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Thank you for using Palindrome Checker!")
            break

        if is_palindrome(user_input):
            print(f"✓ '{user_input}' is a palindrome!")
        else:
            print(f"✗ '{user_input}' is not a palindrome.")


if __name__ == "__main__":
    main()
