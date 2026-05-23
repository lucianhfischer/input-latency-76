import logging

# Configure logging settings
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def log_warning(message):
    logging.warning(message)

# Example of usage in input processing loop
if __name__ == '__main__':
    user_input = 'example'
    if isinstance(user_input, str) and user_input:
        log_info(f'Received valid input: {user_input}')
    else:
        log_error('Invalid input received')
        log_warning('Input should be a non-empty string')
