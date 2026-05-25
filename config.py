import json
import os

class ConfigLoader:
    def __init__(self, default_config_path='default_config.json', user_config_path='user_config.json'):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.load_default_config()
        user_config = self.load_user_config()
        config.update(user_config)
        return config

    def load_default_config(self):
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f'Default config not found at {self.default_config_path}')
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_user_config(self):
        if os.path.exists(self.user_config_path):
            with open(self.user_config_path, 'r') as file:
                return json.load(file)
        return {}

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
# if __name__ == '__main__':
#     config_loader = ConfigLoader()
#     print(config_loader.get('resolution', '1920x1080'))
