import time
import requests

class NetworkError(Exception):
    pass


def retry_request(url, max_retries=5, backoff_factor=0.3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f"Max retries exceeded for {url}") from e
            wait_time = backoff_factor * (2 ** (retries - 1))
            time.sleep(wait_time)  # Exponential backoff

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)
