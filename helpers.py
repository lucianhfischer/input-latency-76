from typing import List, Tuple


def calculate_average_latencies(latencies: List[int]) -> float:
    """Calculates the average latency from a list of latencies.

    Args:
        latencies (List[int]): A list of latency values in milliseconds.

    Returns:
        float: The average latency value.
    """    
    if not latencies:
        return 0.0
    return sum(latencies) / len(latencies)


def find_max_latency(latencies: List[int]) -> Tuple[int, int]:
    """Finds the max latency and its index.

    Args:
        latencies (List[int]): A list of latency values in milliseconds.

    Returns:
        Tuple[int, int]: The maximum latency value and its index.
    """    
    if not latencies:
        return 0, -1
    max_latency = max(latencies)
    max_index = latencies.index(max_latency)
    return max_latency, max_index


def filter_latencies_below_threshold(latencies: List[int], threshold: int) -> List[int]:
    """Filters out latencies below a specified threshold.

    Args:
        latencies (List[int]): A list of latency values in milliseconds.
        threshold (int): The latency threshold for filtering.

    Returns:
        List[int]: A list of latencies above the threshold.
    """    
    return [latency for latency in latencies if latency >= threshold]
