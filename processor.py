from typing import List, Dict
import time

class InputProcessor:
    """
    A class to process game input events, measuring input latency.
    """

    def __init__(self) -> None:
        self.latency_data: List[float] = []

    def record_input_event(self, event: Dict[str, float]) -> None:
        """
        Records an input event and measures latency.
        
        Parameters:
        event (Dict[str, float]): A dictionary containing event details with a 'timestamp'.
        """
        current_time = time.time()
        latency = current_time - event['timestamp']
        self.latency_data.append(latency)

    def average_latency(self) -> float:
        """
        Calculates and returns the average latency from recorded events.
        
        Returns:
        float: The average latency.
        """
        if not self.latency_data:
            return 0.0
        return sum(self.latency_data) / len(self.latency_data)

    def clear_data(self) -> None:
        """
        Clears the recorded latency data.
        """
        self.latency_data.clear()
