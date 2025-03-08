from datetime import datetime
import hashlib

class Transaction:
    def __init__(self, transaction_id, data, size):
        self.transaction_id = transaction_id
        self.timestamp = datetime.now()
        self.data = data
        self.size = size
        self.signature = self._generate_signature()
    
    def _generate_signature(self):
        return hashlib.sha256(f"{self.transaction_id}{self.data}".encode()).hexdigest()
    
    def validate(self):
        return hashlib.sha256(f"{self.transaction_id}{self.data}".encode()).hexdigest() == self.signature