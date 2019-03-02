#This file contains the varous consensus (conflict-resolving) algorithms that the user can choose

class Consensus:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.neighbours = self.blockchain.nodes

        self.length_of_chain = len(self.blockchain.chain)
    
    def longest_chain(self):
        new_chain = None

        for node in self.neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > self.length_of_chain and self.valid_chain(chain):
                    self.length_of_chain = length
                    new_chain = chain
        
        return new_chain