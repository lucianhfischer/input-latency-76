import json
import os

DEFAULT_CONFIG = {
    'resolution': '1920x1080',
    'fullscreen': True,
    'volume': 50,
    'controls': {
        'move_forward': 'W',
        'move_backward': 'S',
        'turn_left': 'A',
        'turn_right': 'D',
    }
}

def load_config(config_file='config.json'):
    """Load configuration from a JSON file, using defaults if not present."""
    if not os.path.exists(config_file):
        return DEFAULT_CONFIG  # Return defaults if file does not exist
    with open(config_file, 'r') as file:
        user_config = json.load(file)  # Load user-defined config
    # Merging user config with defaults
    config = {**DEFAULT_CONFIG, **user_config}
    return config
