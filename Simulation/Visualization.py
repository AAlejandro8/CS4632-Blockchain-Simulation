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
        
        edge_trace = go.Scatter(x=edge_x, y=edge_y, mode='lines')
        node_trace = go.Scatter(x=[pos[n][0] for n in self.network.graph.nodes()],
                              y=[pos[n][1] for n in self.network.graph.nodes()],
                              mode='markers')
        
        fig = go.Figure(data=[edge_trace, node_trace])
        fig.show()