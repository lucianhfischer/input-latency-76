import re

def validate_input(user_input):
    """
    Validates the user input for gaming commands.
    Ensures the input matches expected patterns.
    """
    # Define a pattern for valid commands
    valid_command_pattern = re.compile(r'^(move|attack|defend|item)\s+[\w]+$')
    # Check if the input matches the valid command pattern
    if not valid_command_pattern.match(user_input):
        raise ValueError('Invalid command. Please use: move <direction>, attack <target>, defend, or item <item_name>.')
    return True

# Example usage in the processing loop

def process_user_input(user_input):
    try:
        if validate_input(user_input):
            # Process the valid command
            print(f'Processing command: {user_input}')
    except ValueError as e:
        print(e)

# Simulated game processing loop
if __name__ == '__main__':
    commands = ['move north', 'attack goblin', 'defend', 'item health_potion', 'fly high']
    for command in commands:
        process_user_input(command)