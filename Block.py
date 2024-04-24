import hashlib
import json
from datetime import datetime as time


class Block:
    def __init__(self, data: list, previous_hash: str):
        self.index = 1
        self.timestamp = str( time.now() )
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash( self ) -> object:
        block_string = json.dumps( {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True ).encode( 'utf-8' )
        return hashlib.sha256( block_string ).hexdigest()
   
