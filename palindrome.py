def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]


def main():
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()
