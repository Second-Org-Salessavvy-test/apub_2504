def reverse_string(input_string):
    """
    Reverse a string.

    Args:
        input_string (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string, got {type(input_string).__name__}")

    return input_string[::-1]
