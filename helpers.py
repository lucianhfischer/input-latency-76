import time
import random

class NetworkError(Exception):
    pass

def retry_request(func, retries=3, delay=2):
    """
    Retry a network operation a specified number of times.
    :param func: The network operation to retry.
    :param retries: Number of retry attempts.
    :param delay: Delay between attempts in seconds.
    """
    for attempt in range(retries):
        try:
            return func()
        except NetworkError as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
    raise NetworkError("All retry attempts failed.")

# Example network operation

def mock_network_request():
    """
    Simulates a network request that randomly fails.
    """
    if random.choice([True, False]):
        raise NetworkError("Simulated network failure.")
    return "Success!"

if __name__ == '__main__':
    try:
        result = retry_request(mock_network_request)
        print(result)
    except NetworkError as e:
        print(e)