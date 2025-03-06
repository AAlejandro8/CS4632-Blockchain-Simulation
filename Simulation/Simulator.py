import simpy
import random
from Blockchain.Transaction import Transaction
from Simulation.Data.Metrics import Metrics
import networkx as nx

class Network:
    def __init__(self, topology="random"):
        self.graph = nx.Graph()
        self.topology = topology
        self.node_count = 0
    
    def add_node(self, node):
        self.graph.add_node(node.node_id)
        self.node_count += 1
    
    def remove_node(self, node_id):
        self.graph.remove_node(node_id)
        self.node_count -= 1
    
    def generate_topology(self):
        if self.topology == "random":
            self.graph = nx.random_geometric_graph(self.node_count, 0.3)
    
    def simulate_propagation(self, transaction):
        start_node = random.choice(list(self.graph.nodes))
        self.nodes[start_node].broadcast_transaction(transaction, self)
    
    def simulate_attack(self):
        malicious_node = random.choice(list(self.graph.nodes))
        self.nodes[malicious_node].is_malicious = True

class Simulator:
    def __init__(self, network, simulation_time):
        self.env = simpy.Environment()
        self.network = network
        self.event_queue = []
        self.simulation_time = simulation_time
        self.metrics = Metrics()
    
    def run_simulation(self):
        self.env.process(self._simulation_process())
        self.env.run(until=self.simulation_time)
    
    def _simulation_process(self):
        while True:
            transaction = Transaction(random.randint(1, 1000), "Sample Data", 1024)
            yield self.env.timeout(random.uniform(0.1, 1.0))
            self.network.simulate_propagation(transaction)
            self.record_metrics()

    def record_metrics(self):
        self.metrics.calculate_metrics()