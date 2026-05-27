import time

class InputLatencyProcessor:
    def __init__(self):
        self.latency_records = []

    def add_latency(self, latency):
        if not isinstance(latency, (int, float)):
            raise ValueError("Latency must be a number.")
        if latency < 0:
            raise ValueError("Latency cannot be negative.")
        self.latency_records.append(latency)

    def calculate_average_latency(self):
        if not self.latency_records:
            raise ValueError("No latency data available to calculate average.")
        return sum(self.latency_records) / len(self.latency_records)

    def reset_latencies(self):
        self.latency_records = []

    def get_latency_report(self):
        try:
            average = self.calculate_average_latency()
            return {"average_latency": average, "record_count": len(self.latency_records)}
        except ValueError as e:
            return {"error": str(e)}

# Example Usage:
if __name__ == '__main__':
    processor = InputLatencyProcessor()
    try:
        processor.add_latency(50)
        processor.add_latency(75)
        report = processor.get_latency_report()
        print(report)
    except ValueError as e:
        print(f'Error: {e}')