from Blockchain import Blockchain
from Block import Block

# Create a blockchain instance
blockchain = Blockchain()

# Create blocks and add them to the blockchain
block1 = Block({"amount": 4}, blockchain.get_latest_block().hash)
blockchain.add_block(block1)

block2 = Block({"amount": 10}, blockchain.get_latest_block().hash)
blockchain.add_block(block2)

# Test blockchain validity
#print("Blockchain validity:", blockchain.is_chain_valid())

# Trying to tamper with the blockchain
#blockchain.chain[1].transactions = {"amount": 100}
#blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()

#print("Blockchain validity after tampering:", blockchain.is_chain_valid())

print(blockchain.display_chain())
print(blockchain.last_index())
