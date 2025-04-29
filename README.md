# Blockchain Transaction Propagation Simulation (CS 4632)

## 📊 Overview
This project simulates transaction propagation in peer-to-peer blockchain networks to identify key factors affecting efficiency. By modeling network topology, latency, and bandwidth constraints, this simulation provides insights into decentralized network dynamics and protocol optimization applicable beyond Bitcoin to other blockchain systems.

## 🔍 Research Focus
The simulation examines how different network parameters impact transaction propagation in blockchain networks. The primary goals are to:

1. Analyze the impact of network topology on transaction propagation speed
2. Evaluate how bandwidth constraints affect network throughput
3. Measure the influence of node latency on overall network performance
4. Identify bottlenecks in transaction propagation

## 🌐 Why Small-World Network?
A small-world network topology was selected as the primary model because it closely resembles real-world blockchain networks like Bitcoin and Ethereum. Small-world networks are characterized by:

1. **High Clustering**: Nodes tend to form clusters with their neighbors
2. **Short Path Lengths**: Despite clustering, there are short paths between any two nodes

These properties reflect the structure of actual blockchain networks where:
- Nodes connect to geographically close peers (clustering)
- The network maintains "long-range" connections that ensure quick propagation globally
- Information can efficiently spread despite the network's decentralized nature

Small-world networks represent a balance between completely random networks (which lack realistic clustering) and regular lattice networks (which lack efficient paths). This balance provides an optimal model for studying real-world blockchain transaction propagation.

## 💻 Implementation

### Core Components
- **Node**: Represents network participants with bandwidth, latency, and connectivity attributes
- **Transaction**: Models blockchain transactions with size, signature, and verification methods
- **Network**: Manages the network topology and simulates transaction propagation
- **Simulator**: Orchestrates the simulation environment and events
- **Metrics**: Collects performance data including propagation time and throughput
- **Visualization**: Provides interactive visualization of the network and transaction flow

### Key Features
- ✅ Realistic network topology generation using small-world model
- ✅ Simulation of transaction propagation with bandwidth and latency constraints
- ✅ Interactive visualization of network topology
- ✅ Animation showing transaction propagation between nodes
- ✅ Performance metrics collection and analysis

## 🚀 Running the Simulation
1. Ensure all dependencies are installed: `networkx`, `simpy`, `plotly`
```bash
pip install networkx simpy plotly
```
2. Run the main sim:
```
python main.py
```
3. View the network topology visualization
4. Watch the transaction propagation animation using the play button

## 🔮 Future Enhancements
- Implementation of alternative network topologies (scale-free, random)
- Simulation of network attacks and resistance mechanisms
- Advanced metrics for detailed performance analysis
- Support for different consensus mechanisms and their impact on propagation

## 📊 Overview
This project simulates transaction propagation in peer-to-peer blockchain networks to explore the impact of network structure and communication constraints on performance. Using a small-world topology, the simulation replicates key dynamics of decentralized systems like Bitcoin and Ethereum.

The results provide insights into how topology, latency, and bandwidth affect transaction speed and reliability—offering optimization guidance for blockchain protocols and networking strategies.

