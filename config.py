import json
import os

def load_config(config_file='config.json', defaults=None):
    if defaults is None:
        defaults = {}

    # Check if the config file exists
    if not os.path.isfile(config_file):
        print(f'Config file {config_file} not found. Using defaults. ')
        return defaults

    try:
        with open(config_file, 'r') as f:
            config_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error reading the config file: {e}. Using defaults.')
        return defaults

    # Merge the loaded settings with default settings
    config = {**defaults, **config_data}
    return config

# Example usage
if __name__ == '__main__':
    default_settings = {'resolution': '1920x1080', 'fullscreen': True, 'volume': 75}
    config = load_config('settings.json', default_settings)
    print(config)