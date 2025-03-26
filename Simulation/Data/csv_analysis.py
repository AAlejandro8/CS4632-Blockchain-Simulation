import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the graphs folder exists
os.makedirs("Analysis/graphs", exist_ok=True)

# Load CSV data
csv_file = r"simulation_results.csv"
df = pd.read_csv(csv_file, header=None, names=["Run ID", "Node Count", "Throughput", "Latency"])

# ✅ 1. Throughput vs. Node Count
plt.figure(figsize=(10, 6))
plt.scatter(df["Node Count"], df["Throughput"], color='blue', label="Throughput")
plt.title("Throughput vs. Node Count")
plt.xlabel("Node Count")
plt.ylabel("Throughput (tx/sec)")
plt.grid(True)
plt.legend()
plt.savefig("Analysis/graphs/throughput_vs_nodes.png")
plt.show()

# ✅ 2. Latency vs. Node Count
plt.figure(figsize=(10, 6))
plt.scatter(df["Node Count"], df["Latency"], color='red', label="Latency")
plt.title("Latency vs. Node Count")
plt.xlabel("Node Count")
plt.ylabel("Latency (seconds)")
plt.grid(True)
plt.legend()
plt.savefig("Analysis/graphs/latency_vs_nodes.png")
plt.show()

# ✅ 3. Throughput and Latency Over Time
fig, ax1 = plt.subplots(figsize=(12, 6))

# Throughput Line
color = 'tab:blue'
ax1.set_xlabel('Simulation Step')
ax1.set_ylabel('Throughput (tx/sec)', color=color)
ax1.plot(df.index, df["Throughput"], color=color, label="Throughput")
ax1.tick_params(axis='y', labelcolor=color)

# Latency Line (secondary axis)
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Latency (seconds)', color=color)
ax2.plot(df.index, df["Latency"], color=color, label="Latency")
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title("Throughput and Latency Over Simulation Steps")
plt.savefig("Analysis/graphs/throughput_latency_over_time.png")
plt.show()

print("\n✅ Graphs saved in 'Analysis/graphs/' folder.")
