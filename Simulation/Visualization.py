import plotly.graph_objects as go
import networkx as nx

class Visualization:
    def __init__(self, network, metrics):
        self.network = network
        self.metrics = metrics
    
    def plot_topology(self):
        pos = nx.spring_layout(self.network.graph)
        edge_x = []
        edge_y = []
        
        for edge in self.network.graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        
        node_x = []
        node_y = []
        node_color = []
        node_text = []
        
        for node_id in self.network.graph.nodes():
            x, y = pos[node_id]
            node_x.append(x)
            node_y.append(y)
            
            node = self.network.nodes[node_id]
            if node.is_malicious:
                node_color.append('red')
            else:
                node_color.append('blue')
            
            node_text.append(f"Node ID: {node_id}<br>"
                             f"Bandwidth: {node.bandwidth} Mbps<br>"
                             f"Latency: {node.latency} s<br>"
                             f"Transactions: {node.tx_count}<br>"
                             f"Location: {node.location}")
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            marker=dict(
                size=10,
                color=node_color,
                line=dict(width=2)
            ),
            text=node_text,
            hoverinfo='text'
        )
        
        fig = go.Figure(data=[edge_trace, node_trace])
        
        fig.update_layout(
            title='Blockchain Network Topology',
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
        
        fig.show()