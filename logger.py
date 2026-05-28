import logging

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(f'{name}.log')
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_debug(self, message):
        self.logger.debug(message)

if __name__ == '__main__':
    game_logger = GameLogger('game_events')
    game_logger.log_info('Game initialized successfully.')
    game_logger.log_warning('Low memory warning!')
    game_logger.log_error('Failed to load resource.')
    game_logger.log_debug('Debugging game mechanics.')