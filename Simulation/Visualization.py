import plotly.graph_objects as go
import networkx as nx

class Visualization:
    def __init__(self, network, metrics):
        self.network = network
        self.metrics = metrics
    
    def plot_topology(self):
        # Generate positions for nodes
        pos = nx.spring_layout(self.network.graph)
        
        # Prepare edge coordinates
        edge_x = []
        edge_y = []
        for edge in self.network.graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        # Create edge trace
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        
        # Prepare node coordinates and attributes
        node_x = []
        node_y = []
        node_color = []
        node_text = []
        
        # Process each node
        for node_id in self.network.graph.nodes():
            x, y = pos[node_id]
            node_x.append(x)
            node_y.append(y)
            
            node = self.network.nodes[node_id]
            if node.is_malicious:
                node_color.append('red')
            else:
                node_color.append('blue')
            
            # Create hover text with node info
            node_text.append(f"Node ID: {node.node_id}<br>"
                             f"Bandwidth: {node.bandwidth} Mbps<br>"
                             f"Latency: {node.latency} s<br>"
                             f"Connectivity: {len(node.connectivity)}<br>"
                             f"Malicious: {node.is_malicious}<br>"
                             f"Location: {node.location}<br>"
                             f"Transactions: {node.tx_count}")
        
        # Create node trace
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            marker=dict(size=10, color=node_color, line=dict(width=2)),
            text=node_text,
            hoverinfo='text'
        )
        
        # Create figure and show
        fig = go.Figure(data=[edge_trace, node_trace])
        fig.update_layout(
            title='Blockchain Network Topology',
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
        fig.show()
    
    def animate_propagation(self, transactions):
        # Generate positions for nodes
        pos = nx.spring_layout(self.network.graph)
        
        # Prepare edge coordinates
        edge_x = []
        edge_y = []
        for edge in self.network.graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        # Create edge trace - stays constant in all frames
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        
        # Prepare node coordinates and text - constant in all frames
        node_x = []
        node_y = []
        node_text = []
        default_node_color = []
        
        for node_id in self.network.graph.nodes():
            x, y = pos[node_id]
            node_x.append(x)
            node_y.append(y)
            
            node = self.network.nodes[node_id]
            default_node_color.append('blue')  # Default color
            node_text.append(f"Node ID: {node.node_id}<br>"
                             f"Bandwidth: {node.bandwidth} Mbps<br>"
                             f"Latency: {node.latency} s<br>"
                             f"Connectivity: {len(node.connectivity)}<br>"
                             f"Malicious: {node.is_malicious}<br>"
                             f"Location: {node.location}<br>"
                             f"Transactions: {node.tx_count}")
        
        # Create frames for animation
        frames = []
        
        # Create a frame for each transaction
        for i, tx in enumerate(transactions):
            # Get sender and receiver - transactions should now always have these
            sender_id = tx.sender_id
            receiver_id = tx.receiver_id
            
            # Color nodes based on transaction role
            frame_node_color = default_node_color.copy()
            frame_node_color[sender_id] = 'green'     # Sender
            frame_node_color[receiver_id] = 'yellow'  # Receiver
            
            # Make nodes larger for the active transaction to make it more obvious
            node_sizes = [10] * len(node_x)
            node_sizes[sender_id] = 20
            node_sizes[receiver_id] = 20
            
            # Create node trace for this frame
            frame_node_trace = go.Scatter(
                x=node_x, y=node_y,
                mode='markers',
                marker=dict(size=node_sizes, color=frame_node_color, line=dict(width=2)),
                text=node_text,
                hoverinfo='text'
            )
            
            # Add annotation to show current transaction
            tx_info = go.layout.Annotation(
                text=f"Transaction {i}: Node {sender_id} → Node {receiver_id}",
                align="left",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.5,
                y=1.05,
                bordercolor="black",
                borderwidth=1
            )
            
            # Add frame
            frames.append(go.Frame(
                data=[edge_trace, frame_node_trace],
                name=str(i),  # Important: name is used by slider
                layout=dict(annotations=[tx_info])
            ))
        
        # Create initial figure with first frame
        fig = go.Figure(
            data=[edge_trace, go.Scatter(
                x=node_x, y=node_y,
                mode='markers',
                marker=dict(size=10, color=default_node_color, line=dict(width=2)),
                text=node_text,
                hoverinfo='text'
            )],
            frames=frames
        )
        
        # Add play button and slider
        fig.update_layout(
            title='Transaction Propagation Animation',
            updatemenus=[{
                'type': 'buttons',
                'buttons': [{
                    'label': 'Play',
                    'method': 'animate',
                    'args': [None, {
                        'frame': {'duration': 1500, 'redraw': True},  # Longer duration for more noticeable movement
                        'fromcurrent': True,
                        'transition': {'duration': 500, 'easing': 'cubic-in-out'}  # Add transition effect
                    }]
                }],
                'direction': 'left',
                'pad': {'r': 10, 't': 10},
                'showactive': False,
                'x': 0.1,
                'y': 0,
                'xanchor': 'right',
                'yanchor': 'top'
            }],
            sliders=[{
                'active': 0,
                'yanchor': 'top',
                'xanchor': 'left',
                'currentvalue': {
                    'font': {'size': 16},
                    'prefix': 'Transaction: ',
                    'visible': True,
                    'xanchor': 'center'
                },
                'steps': [{'args': [[f.name], {
                                'frame': {'duration': 1000, 'redraw': True},
                                'mode': 'immediate',
                                'transition': {'duration': 300}
                            }],
                           'label': f"{i}",
                           'method': 'animate'} for i, f in enumerate(frames)],
                'x': 0.1,
                'y': 0,
                'len': 0.9
            }]
        )
        
        # Show animated figure
        fig.show()