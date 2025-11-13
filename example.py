from utils import reverse_string


def main():
    test_strings = [
        "hello",
        "Python",
        "hello world",
        "racecar",
        "12345",
        "!@#$%",
    ]

    print("String Reversal Examples:")
    print("-" * 40)

    for test_str in test_strings:
        reversed_str = reverse_string(test_str)
        print(f'"{test_str}" -> "{reversed_str}"')


if __name__ == "__main__":
    main()
