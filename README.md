# input-latency-76

input-latency-76 is a Python tool designed to measure and analyze input latency in gaming setups. By providing real-time feedback and detailed reports, developers and gamers can fine-tune their hardware and software for optimal performance.

## Features

- **Comprehensive Latency Measurement**: Accurately captures the time from user input to system reaction, allowing for precise calibration of gaming setups.
- **Real-Time Visualization**: Provides a graphical representation of latency data, making it easy to identify spikes and trends during gameplay.
- **Customizable Testing Scenarios**: Users can configure settings for different input devices (keyboard, mouse, gamepad) and test under various conditions.
- **Exportable Reports**: Generate CSV reports of latency metrics for further analysis or comparison, aiding in troubleshooting and optimization.

## Installation

To get started with input-latency-76, follow these straightforward installation steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Developer/input-latency-76.git
   cd input-latency-76
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Basic Usage Example

Once installed, you can run the tool as follows:

```python
from latency_tester import LatencyTester

tester = LatencyTester(input_device='mouse')
results = tester.run_test(duration=30)  # Test for 30 seconds
tester.display_results()
```

This will begin a latency test for the specified input device and display the results, helping you understand performance metrics during gameplay.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)