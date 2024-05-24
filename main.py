import hashlib
from datetime import datetime

class Block:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.h_date = datetime.today()
        self.transaction_list = transaction_list
        self.block_data = f"{' - '.join(transaction_list)}-  {self.h_date} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(Block("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(Block(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Block {i + 1} Data: {self.chain[i].block_data}")
            print(f"Block {i + 1} Hash: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]

# Exemple d'utilisation
t1 = "George envoie 3.1 GC à Joe"
t2 = "Joe envoie 2.5 GC à Adam"
t3 = "Adam envoie 1.2 GC à Bob"
t4 = "Bob envoie 0.5 GC à Charlie"
t5 = "Charlie envoie 0.2 GC à David"
t6 = "David envoie 0.1 GC à Eric"


myblockchain = Blockchain() # type: ignore



myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])


myblockchain.display_chain()
