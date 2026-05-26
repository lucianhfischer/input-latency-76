import sys
import json

# Define a simple custom exception for validation errors
class ValidationError(Exception):
    pass

# Function to validate user input
def validate_input(user_input):
    if not isinstance(user_input, dict):
        raise ValidationError('Input must be a dictionary.')
    required_keys = ['action', 'value']
    for key in required_keys:
        if key not in user_input:
            raise ValidationError(f'Missing required key: {key}')
    if not isinstance(user_input['value'], int):
        raise ValidationError('Value must be an integer.')
    return True

# Main processing loop
def main_loop():
    while True:
        try:
            # Simulated user input
            user_input = json.loads(input('Enter input (JSON): '))
            validate_input(user_input)  # Validate input
            process_input(user_input)  # Process validated input
        except ValidationError as ve:
            print(f'Validation Error: {ve}')
        except json.JSONDecodeError:
            print('Invalid JSON format.')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

# Function to process validated input
def process_input(user_input):
    print(f'Processing action: {user_input['action']} with value: {user_input['value']}')

if __name__ == '__main__':
    main_loop()