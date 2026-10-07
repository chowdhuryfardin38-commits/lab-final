def analyze_digits_and_case(user_input: str) -> tuple:
    """
    Analyzes a given string by stripping leading/trailing whitespaces,
    counting total uppercase letters, and summing all numeric digits present.
    Returns (uppercase_count, digit_sum). Returns (0, 0) if empty or no matches.
    """
    if not user_input:
        return (0, 0)

    cleaned_input = user_input.strip()
    if not cleaned_input:
        return (0, 0)

    uppercase_count = sum(1 for char in cleaned_input if char.isupper())
    digit_sum = sum(int(char) for char in cleaned_input if char.isdigit())

    return (uppercase_count, digit_sum)
