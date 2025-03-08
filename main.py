import random
from Blockchain.Node import Node
from Simulation.Simulator import Network, Simulator
from Simulation.Visualization import Visualization

if __name__ == "__main__":
    # Create network
    network = Network("random")
    
    # Add nodes
    for i in range(10):
        node = Node(i, bandwidth=1000, latency=0.1, location=(random.random(), random.random()))
        network.add_node(node)
    
    network.generate_topology()
    
    # Create simulator
    simulator = Simulator(network, 10)
    
    # Create visualization
    vis = Visualization(network, simulator.metrics)
    
    # Run simulation and visualize
    simulator.run_simulation()
    vis.plot_topology()