import simpy
import random
from Blockchain.Transaction import Transaction
from Simulation.Data.Metrics import Metrics
import networkx as nx

class Network:
    def __init__(self, topology="small_world"):
        self.graph = nx.Graph()
        self.topology = topology
        self.node_count = 0
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node):
        self.graph.add_node(node.node_id)
        self.node_count += 1
        self.nodes[node.node_id] = node
    
    def generate_topology(self):
        if self.topology == "small_world":
            self.graph = nx.watts_strogatz_graph(self.node_count, k=4, p=0.1)
            for edge in self.graph.edges():
                self.nodes[edge[0]].connect_to_node(edge[1])
                self.nodes[edge[1]].connect_to_node(edge[0])
                self.edges.append((edge[0], edge[1]))
    
    def simulate_propagation(self, transaction):
        start_node = random.choice(list(self.graph.nodes))
        visited = set([start_node])
        to_visit = [(start_node, 0)]  # (node_id, delay)
        
        while to_visit:
            current_node, current_delay = to_visit.pop(0)
            
            # Apply the accumulated delay
            if current_delay > 0:
                yield self.simulator.env.timeout(current_delay)
            
            # Process the node
            if self.nodes[current_node].receive_transaction(transaction):
                # Propagate to neighbors with bandwidth and latency constraints
                for neighbor in self.graph.neighbors(current_node):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        
                        # Calculate delay based on both sending and receiving nodes
                        sender = self.nodes[current_node]
                        receiver = self.nodes[neighbor]
                        
                        # Base latency (network delay)
                        base_latency = sender.latency + receiver.latency
                        
                        # Transmission time based on bandwidth (in seconds)
                        # Formula: (message size in KB) / (bandwidth in MB/s) * (1000 KB/MB)
                        bandwidth_delay = transaction.size / (min(sender.bandwidth, receiver.bandwidth) / 1000)
                        
                        # Total delay
                        total_delay = base_latency + bandwidth_delay
                        
                        # Add to queue with calculated delay
                        to_visit.append((neighbor, total_delay))

class Simulator:
    def __init__(self, network, simulation_time):
        self.env = simpy.Environment()
        self.network = network
        self.simulation_time = simulation_time
        self.metrics = Metrics()
        self.transactions = {}
        self.network.simulator = self  # Link back to simulator
    
    def run_simulation(self):
        self.env.process(self._simulation_process())
        self.env.run(until=self.simulation_time)
    
    def _simulation_process(self):
        while True:
            # Create transaction with random ID
            transaction = Transaction(random.randint(1, 1000), "Sample Data", random.uniform(1.0, 10.0))
            
            # Assign random sender and receiver that are different nodes
            all_nodes = list(self.network.nodes.keys())
            transaction.sender_id = random.choice(all_nodes)
            
            # Make sure receiver is different from sender
            remaining_nodes = [n for n in all_nodes if n != transaction.sender_id]
            
            if remaining_nodes:  # Ensure there are other nodes
                transaction.receiver_id = random.choice(remaining_nodes)
            else:
                transaction.receiver_id = transaction.sender_id  # Fallback if only one node
            
            # Store transaction and simulate propagation
            self.transactions[transaction.transaction_id] = transaction
            self.env.process(self.network.simulate_propagation(transaction))
            
            # Wait before next transaction
            yield self.env.timeout(random.uniform(0.5, 2.0))
            
            # Update metrics
            self.metrics.calculate_metrics()