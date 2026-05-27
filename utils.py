import time
from functools import wraps

# A decorator to benchmark function execution time
def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

# A utility function to calculate the average of a list
def calculate_average(data):
    if not data:
        return 0
    return sum(data) / len(data)

# A function to optimize data processing
@benchmark
def process_data(data):
    optimized_data = sorted(set(data))  # Removes duplicates and sorts
    return calculate_average(optimized_data)
