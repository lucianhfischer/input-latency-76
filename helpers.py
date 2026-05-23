import time
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class InputLatencyError(Exception):
    pass

def validate_input_time(input_time):
    if not isinstance(input_time, (int, float)):
        logging.error('Invalid input type: %s', type(input_time))
        raise InputLatencyError('Input time must be an integer or float')
    if input_time < 0:
        logging.error('Negative input time: %s', input_time)
        raise InputLatencyError('Input time cannot be negative')
    logging.debug('Input time validated: %s', input_time)
    return input_time

def simulate_input_latency(input_time):
    validate_input_time(input_time)
    try:
        logging.info('Starting latency simulation for: %s seconds', input_time)
        time.sleep(input_time)
        logging.info('Latency simulation completed')
    except Exception as e:
        logging.error('Error during latency simulation: %s', str(e))
        raise InputLatencyError('Simulation failed due to an unexpected error')

# Example usage
if __name__ == '__main__':
    try:
        simulate_input_latency(0.5)
    except InputLatencyError as e:
        logging.error('InputLatencyError: %s', e)