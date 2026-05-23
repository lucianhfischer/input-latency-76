import time
import random

MAX_RETRIES = 5
RETRY_DELAY = 2  # seconds

class NetworkError(Exception):
    pass

def simulated_network_operation():
    if random.random() < 0.7:  # Simulating a failure 70% of the time
        raise NetworkError("Network operation failed")
    return "Success"

def perform_network_operation_with_retries():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            result = simulated_network_operation()
            print(result)
            return result
        except NetworkError as e:
            print(f'Attempt {attempt} failed: {e}')
            time.sleep(RETRY_DELAY)
            if attempt == MAX_RETRIES:
                print('All attempts failed.')
                raise

if __name__ == '__main__':
    perform_network_operation_with_retries()