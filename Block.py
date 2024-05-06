import hashlib
import json
from datetime import datetime as time


class Block:
    def __init__(self, data: str, previous_hash: str):
        self.__index = 1
        self.__timestamp = str( time.now() )
        self.__data = data
        self.__previous_hash = previous_hash
        self.__nonce = 0
        self.__hash = self.calculate_hash()

    def calculate_hash( self ) -> object:
        block_string = json.dumps( {
            "index": self.__index,
            "timestamp": self.__timestamp,
            "data": self.__data,
            "previous_hash": self.__previous_hash,
            "nonce": self.__nonce
        }, sort_keys=True ).encode( 'utf-8' )
        return hashlib.sha256( block_string ).hexdigest()
  
    # set and get INDEX
    def set_index( self, new_index: int ):
        self.__index = new_index
    
    def get_index( self ) -> int:
        return self.__index 
  
    # set and get TIMESTAMP
    def set_timestamp( self ):
        self.__timestamp = str( time.now() )
        
    def get_timestamp( self ) -> str :
        return self.__timestamp
    
    # set and get DATA
    def set_data( self, new_data: str ):
        self.__data = new_data
        
    def get_data( self ) -> str :
        return self.__data 
    
    # set and get PREVIOUS HASH
    def set_previous_hash( self, new_previous_hash ):
        self.__previous_hash = new_previous_hash
        
    def get_previous_hash( self ) -> str:
        return self.__previous_hash
    
    # set and get HASH
    def set_hash( self, new_hash ):
        self.__hash = new_hash
        
    def get_hash( self ) -> object:
        return self.__hash