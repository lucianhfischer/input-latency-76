import random
import time

def generate_random_number(min_value, max_value):
    """Generates a random number between min_value and max_value."""
    return random.randint(min_value, max_value)


def simulate_input_latency(latency_ms):
    """Simulates user input delay."""
    time.sleep(latency_ms / 1000.0)


def adjust_latency_for_performance(fps):
    """Adjusts latency based on frames per second (FPS)."""
    if fps < 30:
        return 150  # high latency
    elif fps < 60:
        return 100  # moderate latency
    else:
        return 50   # low latency


def create_latency_banner(latency):
    """Creates a formatted banner displaying the current latency."""
    return f"Current Input Latency: {latency}ms"


def calculate_average_latency(latencies):
    """Calculates the average of a list of latencies."""
    if not latencies:
        return 0
    return sum(latencies) / len(latencies)