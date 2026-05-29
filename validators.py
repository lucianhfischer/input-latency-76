import re

# Regular expression for input validation
VALID_INPUT_PATTERN = re.compile(r'^[a-zA-Z0-9_]+$')

def validate_input(user_input):
    """
    Validates the user's input to ensure it only contains 
    alphanumeric characters and underscores.
    """
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not VALID_INPUT_PATTERN.match(user_input):
        raise ValueError('Input contains invalid characters.')
    return True

# Example usage in main processing loop
if __name__ == '__main__':
    user_input = input('Enter your input: ')
    try:
        if validate_input(user_input):
            print('Input is valid!')
    except ValueError as e:
        print(f'Error: {e}')