from Block import Block
from Color import Color


class Blockchain:
    def __init__( self ):
        self.chain = [ self.create_block() ]

    def create_block( self ) -> Block:
        return Block( [], "0" )

    # return the last block of the chain
    def get_latest_block( self ) -> int:
        return self.chain[ -1 ]

    # add a new block in the chain
    def add_block( self, new_block ):
        new_block.previous_hash = self.get_latest_block().get_hash()
        new_block.set_index( self.last_index() + 1 )
        new_block.hash = new_block.calculate_hash()
        self.chain.append( new_block )

    # valid the chain
    def is_chain_valid( self ) -> bool:
        for i in range( 1, len( self.chain ) ):
            current_block = self.chain[ i ]
            previous_block = self.chain[ i - 1 ]
            if current_block.get_hash() != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.get_hash():
                return False
        return True
   
    # return the last block index
    def last_index( self ) -> int:
         return self.chain[ -1 ].get_index()
   
    #display information of the chain
    def display_chain( self ):
        color = Color()
        h = ''
        for block in self.chain:
            h = f'{ color.red() } Block Index: { block.get_index() } \n'
            h += f'{ color.green() } Timestamp: { block.get_timestamp() } \n'
            h += f'{ color.magenta() } data: { block.get_data() } \n'
            h += f'{ color.yellow() } Block Hash: { block.get_hash() } \n'
            h += f'{ color.cyan() } Previous Hash: { block.get_previous_hash() } \n'
            h += f'{ color.white() } ${ "-" * 79 }$ { color.reset() }'
            print( h )
