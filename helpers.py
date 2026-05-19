import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    """Retry a network request up to max_retries times."""
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for 4xx/5xx responses
            return response.json()  # Returning JSON if request is successful
        except RequestException as e:
            attempts += 1
            print(f'Attempt {attempts} failed: {e}')
            if attempts < max_retries:
                time.sleep(delay)  # Wait before retrying
            else:
                raise  # Reraise the last exception if no attempts left

# Example usage:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print('Data fetched:', data)
    except Exception as error:
        print('Final error after retries:', error)
