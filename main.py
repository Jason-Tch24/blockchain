import hashlib
from datetime import datetime

#Creation de la class des block de la chaine
class Block:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.h_date = datetime.today() #date de creation de la block
        self.transaction_list = transaction_list
        self.block_data = f"{' - '.join(transaction_list)}- {self.h_date} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# la classe blockchain sera responsable de la gestion de la chaine de blocs.
class Blockchain:
    def __init__(self): # initialise la blockchain avec un bloc de genese
        self.chain = [] # type: ignore

        self.generate_genesis_block() # type: ignore

    def generate_genesis_block(self):
        self.chain.append(Block("0", ['Genesis Block']))

    def create_block_from_transaction(self, transaction_list): # ajoute un nouveau bloc à la chaine à partir d'une chaine de transaction
        previous_block_hash = self.last_block.block_hash
        self.chain.append(Block(previous_block_hash, transaction_list))

    def display_chain(self): # affiche tout les blocs 
        for i, block in enumerate(self.chain):
            print(f"Données {i + 1} : {block.block_data}")
            print(f"Hash {i + 1} : {block.block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]
    # Exemple d'uutilisation 

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