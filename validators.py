def validate_input(user_input):
    """
    Validates user input for correctness
    and prevents injection attacks.
    """
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) == 0:
        raise ValueError("Input cannot be empty.")
    if user_input.strip() == '':
        raise ValueError("Input cannot be just whitespace.")
    restricted_chars = [';', '--', '/*', '*/']
    for char in restricted_chars:
        if char in user_input:
            raise ValueError(f"Input contains invalid characters: {char}")
    return True

def main_loop():
    while True:
        user_input = input("Enter your command:")
        try:
            validate_input(user_input)
            # Process the validated input here
            print(f"Processing: {user_input}")
        except ValueError as e:
            print(f"Input error: {e}")

if __name__ == '__main__':
    main_loop()