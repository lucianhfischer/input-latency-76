import json
import time
from typing import Any, Dict, List

class InputLatencyError(Exception):
    pass

def calculate_input_latency(event_time: float, start_time: float) -> float:
    if event_time < start_time:
        raise InputLatencyError('Event time cannot be earlier than start time.')
    return event_time - start_time

def log_latency(latency: float) -> None:
    if latency < 0:
        raise InputLatencyError('Latency must be a non-negative value.')
    print(f'Input latency: {latency:.3f} seconds')

def monitor_input_events(events: List[Dict[str, Any]]) -> None:
    if not events:
        raise InputLatencyError('Event list cannot be empty.')
    start_time = time.time()

    for event in events:
        event_time = event.get('timestamp')
        if event_time is None:
            raise InputLatencyError('Event dictionary must contain a timestamp key.')
        try:
            latency = calculate_input_latency(event_time, start_time)
            log_latency(latency)
        except InputLatencyError as e:
            print(f'Error: {e}')