#!/usr/bin/env python3

def reverse_string(text: str) -> str:
    """
    Reverse a given string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string
    """
    return text[::-1]


def main():
    import sys

    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
    else:
        input_text = input("Enter a string to reverse: ")

    reversed_text = reverse_string(input_text)
    print(f"Original: {input_text}")
    print(f"Reversed: {reversed_text}")


if __name__ == "__main__":
    main()
