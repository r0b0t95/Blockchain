import hashlib
import json
from time import time

class Block:
    def __init__( self, transactions: list, previous_hash: str ):
        self.index = 0
        self.timestamp = time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash( self ) -> object:
        block_string = json.dumps( {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True ).encode( 'utf-8' )
        return hashlib.sha256( block_string ).hexdigest()
   
