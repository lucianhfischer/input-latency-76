import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10 * 1024 * 1024, backup_count=5):
    """
    Set up a logger that saves logs to a file with rotation.
    
    Parameters:
    log_file (str): Name of the log file.
    max_bytes (int): Max size of log file before rotation.
    backup_count (int): Number of backup files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # Create a formatter that adds timestamps and log levels to messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Create a rotating file handler
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage of the logger
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger has been set up.')