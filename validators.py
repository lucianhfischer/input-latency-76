def validate_input(input_value):
    if not isinstance(input_value, (int, float)):
        raise ValueError("Input must be a number.")
    if input_value < 0:
        raise ValueError("Input must be non-negative.")
    return True

def validate_key_press(key):
    valid_keys = {'W', 'A', 'S', 'D', 'SPACE', 'ESC'}
    if key not in valid_keys:
        raise ValueError(f"Invalid key press: {key}")
    return True

# Main processing loop (example usage)
if __name__ == '__main__':
    inputs = [0, 1, -3, 5, 'A', 'Z']  # Example inputs
    for inp in inputs:
        try:
            if isinstance(inp, str):  # Check if input is key press
                validate_key_press(inp)
            else:
                validate_input(inp)
            print(f"Input {inp} is valid.")
        except ValueError as e:
            print(f"Error: {e}")
