import random
from Blockchain.Node import Node
from Blockchain.Transaction import Transaction
from Simulation.Simulator import Network, Simulator
from Simulation.Visualization import Visualization

if __name__ == "__main__":
    # Create network
    network = Network("small_world")
    
    # Add nodes
    for i in range(10):
        node = Node(i, bandwidth=random.uniform(1, 100), latency=random.uniform(0.01, 0.5), location=(random.random(), random.random()))
        network.add_node(node)
    
    network.generate_topology()
    
    # Create simulator
    simulator = Simulator(network, 10)
    
    # Run simulation
    simulator.run_simulation()
    
    # Log the results of the simulation
    run_id = 1  # Example run ID
    simulator.log_run(run_id)
    
    # Create visualization
    vis = Visualization(network, simulator.metrics)
    
    # Visualize topology
    vis.plot_topology()
    
    # Use actual transactions from the simulation for animation
    transactions = list(simulator.transactions.values())
    
    # Animate transaction propagation
    vis.animate_propagation(transactions)