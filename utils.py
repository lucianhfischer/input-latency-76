import json

class GameDataError(Exception):
    """Custom exception for game data handling errors."""
    pass


def load_game_data(file_path):
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise GameDataError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise GameDataError(f"Invalid JSON in file: {file_path}")


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        raise GameDataError(f"Error writing to file: {file_path}")


def validate_game_data(data):
    """Basic validation for game data structure."""
    required_keys = ['player_id', 'score', 'level']
    for key in required_keys:
        if key not in data:
            raise GameDataError(f"Missing required key: {key}")
    return True