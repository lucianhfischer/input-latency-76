import time
import random

class GameLatencySimulator:
    def __init__(self):
        self.latency = 0

    def set_latency(self, min_latency: float, max_latency: float):
        """Set random latency within a given range."""
        self.latency = random.uniform(min_latency, max_latency)

    def simulate_action(self):
        """Simulates an action with latency."""
        time.sleep(self.latency)

    def get_current_latency(self):
        """Returns the current latency."""
        return self.latency

# Example usage:
if __name__ == '__main__':
    simulator = GameLatencySimulator()
    simulator.set_latency(0.1, 0.5)
    print(f'Simulated latency: {simulator.get_current_latency()} seconds')
    simulator.simulate_action()
    print('Action simulated with latency')
