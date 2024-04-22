from Block import Block
from Color import Color
from time import time

class Blockchain:
    def __init__( self ):
        self.chain = [ self.create_block() ]

    def create_block( self ) -> Block:
        return Block( [], "0" )

    def get_latest_block( self ) -> int:
        return self.chain[ -1 ]

    def add_block( self, new_block ):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append( new_block )

    def is_chain_valid( self ) -> bool:
        for i in range( 1, len( self.chain ) ):
            current_block = self.chain[ i ]
            previous_block = self.chain[ i - 1 ]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
   
    def last_index( self ) -> int:
         return self.chain[ -1 ].index
   
    def display_chain( self ):
        color = Color()
        h = ''
        for block in self.chain:
            h = f'{ color.red } Block Index: { block.index } \n'
            h += f'{ color.green } Timestamp: { block.timestamp } \n'
            h += f'{ color.magenta } Transactions: { block.transactions } \n'
            h += f'{ color.yellow } Block Hash: { block.hash } \n'
            h += f'{ color.cyan } Previous Hash: { block.previous_hash } \n'
            h += f'{ color.white } ${ "-" * 79 }$ { color.reset }'
            print( h )


