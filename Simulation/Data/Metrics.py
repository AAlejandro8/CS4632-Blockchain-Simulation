import random

class Metrics:
    def __init__(self):
        self.propagation_times = []
        self.throughput = 0
        self.latency = 0
    
    def calculate_metrics(self):
        self.throughput += 1
        self.latency = random.uniform(0.1, 0.5)