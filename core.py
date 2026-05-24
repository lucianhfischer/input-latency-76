import time
import numpy as np

class GameCore:
    def __init__(self):
        self.frame_data = []
        self.latency_threshold = 0.05  # seconds

    def add_frame(self, frame):
        current_time = time.time()
        if self.should_process_frame(current_time):
            self.frame_data.append((current_time, frame))
            self.process_frame(frame)
        else:
            print("Frame dropped due to high latency.")

    def should_process_frame(self, current_time):
        if not self.frame_data:
            return True
        last_frame_time = self.frame_data[-1][0]
        return (current_time - last_frame_time) < self.latency_threshold

    def process_frame(self, frame):
        # Simulate frame processing
        processed_frame = np.array(frame) * 2  # Example processing operation
        self.display_frame(processed_frame)

    def display_frame(self, frame):
        print(f"Displaying frame: {frame}")

# Example usage
if __name__ == '__main__':
    core = GameCore()
    for i in range(10):
        time.sleep(0.02)  # Simulating a frame render every 20 ms
        core.add_frame(i)
