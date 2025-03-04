import hashlib

class Node:
    def __init__(self, node_id, bandwidth, latency, location):
        self.node_id = node_id
        self.bandwidth = bandwidth
        self.latency = latency
        self.connectivity = []
        self.is_malicious = False
        self.location = location
    
    def broadcast_transaction(self, transaction, network):
        # check if the node is a bad apple
        if not self.is_malicious:
            for connected_node in self.connectivity:
                network.nodes[connected_node].receive_transaction(transaction)
                
    def receive_transaction(self, transaction):
        if self.validate_transaction(transaction):
            return True
        return False
    
    def validate_transaction(self, transaction):
        return transaction.validate()
    
    def connect_to_node(self, node_id):
        if node_id not in self.connectivity:
            self.connectivity.append(node_id)
    
    def disconnect_from_node(self, node_id):
        if node_id in self.connectivity:
            self.connectivity.remove(node_id)