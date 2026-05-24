from typing import List, Tuple


def calculate_average_ping(pings: List[int]) -> float:
    """
    Calculate the average ping from a list of pings.

    Args:
        pings (List[int]): A list of ping values in milliseconds.

    Returns:
        float: The average ping value rounded to two decimal places.
    """    
    if not pings:
        raise ValueError('Ping list cannot be empty')
    return round(sum(pings) / len(pings), 2)


def categorize_ping(ping: int) -> str:
    """
    Categorize the given ping value into latency categories.

    Args:
        ping (int): Ping value in milliseconds.

    Returns:
        str: A category of the ping ('Good', 'Average', 'Poor').
    """    
    if ping < 20:
        return 'Good'
    elif 20 <= ping < 50:
        return 'Average'
    else:
        return 'Poor'


def is_ping_acceptable(ping: int, threshold: int = 100) -> bool:
    """
    Check if the ping is below the acceptable threshold.

    Args:
        ping (int): Ping value in milliseconds.
        threshold (int, optional): The accepted threshold for ping. Defaults to 100.

    Returns:
        bool: True if the ping is acceptable, False otherwise.
    """    
    return ping < threshold
