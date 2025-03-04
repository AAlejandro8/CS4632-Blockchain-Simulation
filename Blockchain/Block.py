from datetime import datetime

class Block:
      def __init__(self, block_id, prev_block_hash):
            self.block_id = block_id
            self.prev_block_hash = prev_block_hash
            self.transactions = []
            self.timestamp = datetime.now()
      
      def validate_block(self):
            return all(trans.validate() 
                       for trans in self.transactions)
