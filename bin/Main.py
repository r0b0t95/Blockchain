from Blockchain import Blockchain
from Block import Block
import sys

option = ' display chain [1] \n is the chain valid [2] \n get the last block [3] \n add a block [4] \n exit [5] \n TYPE A NUMBER:'

if __name__ == '__main__':

     num = ''
     blockchain = Blockchain() 
     
     while True:
          num = input( option )
          if num == '1':
               blockchain.display_chain()
          elif num == '2':
               print( f'Is the chain valid: { blockchain.is_chain_valid() }' )
          elif num == '3':
               print( blockchain.get_latest_block() )
          elif num == '4':
               data = int(input('data: '))
               block = Block( str( data ), blockchain.get_latest_block().get_hash() )
               blockchain.add_block( block )
          else:
               print( '\n\n [-] Exit... ' )
               sys.exit(0)
     
