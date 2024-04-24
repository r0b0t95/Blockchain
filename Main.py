from Blockchain import Blockchain
from Block import Block
import sys


if __name__ == '__main__':

     num = ''
     blockchain = Blockchain() 
     
     while True:
          num = input('type a number: ')
          if num == '1':
               blockchain.display_chain()
          elif num == '2':
               print(f'Is the chain valid: {blockchain.is_chain_valid()}')
          elif num == '3':
               print( blockchain.get_latest_block() )
          elif num == '4':
               data = int(input('data: '))
               block = Block( { 'data': data }, blockchain.get_latest_block().hash )
               blockchain.add_block( block )
          else:
               print( '\n\n [-] Exit... ' )
               sys.exit(0)
     
