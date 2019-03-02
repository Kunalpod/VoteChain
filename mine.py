class Mine:
    
    def __init__(self, blockchain, node_identifier):
        self.blockchain = blockchain
        self.node_identifier = node_identifier

        self.prev_block = self.blockchain.chain[-1]
        self.proof = self.blockchain.proof_of_work(self.prev_block)
    
    def mine(self):
        #Construct new block and add it to the chain
        prev_hash = self.blockchain.hash(self.prev_block)
        block = self.blockchain.new_block(self.proof, prev_hash)

        response = {
            'message': "New Block Created",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'prev_hash': block['prev_hash'],
        }
        return response