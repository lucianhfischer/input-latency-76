import json

class GameDataError(Exception):
    """Custom exception for game data errors."""
    pass


def load_game_data(file_path):
    """Load game data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise GameDataError(f"File '{file_path}' not found.")
    except json.JSONDecodeError:
        raise GameDataError(f"File '{file_path}' contains invalid JSON.")


def save_game_data(file_path, data):
    """Save game data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise GameDataError(f"An error occurred while saving data: {e}")


def update_game_data(file_path, new_data):
    """Update existing game data with new data."""
    try:
        existing_data = load_game_data(file_path)
        existing_data.update(new_data)
        save_game_data(file_path, existing_data)
    except GameDataError as e:
        raise GameDataError(f"Failed to update game data: {e}")
