import unittest
from ..bin.Blockchain import Blockchain

# command -> python -m unittest Blockchain_test.py

blockchain = Blockchain() 

class MyTest( unittest.TestCase ):
    def test_validation( self ):
         
        self.assertEqual( True, blockchain.is_chain_valid() )
        
        