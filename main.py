import random
import os
from Blockchain.Node import Node
from Blockchain.Transaction import Transaction
from Simulation.Simulator import Network, Simulator
from Simulation.Visualization import Visualization

# Ensure the data folder exists
os.makedirs("Simulation/Data", exist_ok=True)

# ✅ Function to run multiple simulations with varying node counts
def run_multiple_simulations(node_counts, sim_time=10, iterations=3):
    for node_count in node_counts:
        print(f"\nRunning simulations with {node_count} nodes...")
        
        for run_id in range(1, iterations + 1):
            # 1. Create network
            network = Network("small_world")

            # 2. Add nodes dynamically
            for i in range(node_count):
                node = Node(
                    node_id=i,
                    bandwidth=random.uniform(10, 100),  # Increased minimum bandwidth for better data collection
                    latency=random.uniform(0.01, 0.25),  # Reduced max latency for better data collection
                    location=(random.random(), random.random())
                )
                network.add_node(node)

            # 3. Generate topology
            network.generate_topology()

            # 4. Create simulator
            simulator = Simulator(network, simulation_time=sim_time)

            # 5. Run the simulation
            simulator.run_simulation()

            # 6. Log the simulation results to CSV
            simulator.log_run(run_id)

            print(f"Simulation with {node_count} nodes (Run {run_id}) completed!")

# ✅ Run multiple simulations with different node counts
if __name__ == "__main__":
    node_ranges = [10, 15, 20, 25]  # Test 10, 15, 20, and 25 nodes, change as needed for more data collection!
    run_multiple_simulations(node_ranges, sim_time=10, iterations=5)

    print("\n✅ All simulations completed. Data saved to CSV.")
