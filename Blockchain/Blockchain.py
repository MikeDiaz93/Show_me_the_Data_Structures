from datetime import datetime
import hashlib

# We can break the blockchain down into three main parts.
# First is the information hash:


class Block:
    """
    Class Block 
        methods:
            __init__ -> Init the Block 
            calc_hash -> Calculates the hash
            __str__ -> Build the str Block 
    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        # self.previous
        return 'Block :' + self.hash + ',timestamp: ' + str(self.timestamp) + ', data: ' + self.data + ',prev.hash' + self.previous_hash


class BlockChain:

    def __init__(self):
        self.root = None
        self.length = 0

    def add_block(self, data=None):
        """
        Add block function:  Add bock of Blockchain
        Input: 
            self and data 
        Output:
            Messages: If it cant add block      
        """
        now = datetime.now()

        if data == None:
            print("Can't add block without data")
            return

        if data == '':
            print("Can't add block as a space str")
            return

        if self.root == None:
            self.root = Block(datetime.timestamp(now),
                              data, previous_hash=None)
        else:
            aux = self.root
            while aux.next:
                aux = aux.next
            previous_hash = aux.calc_hash()
            aux.next = Block(datetime.timestamp(now), data, previous_hash)

        self.length += 1

    def __str__(self):

        if self.root == None:
            return 'The block doesnt exist'
        else:
            aux = self.root

        strg = ''
        index = 0
        while aux:
            strg += 'Index: ' + str(index) + '\n'
            strg += 'Timestamp: ' + str(aux.timestamp) + '\n'
            strg += 'Data: ' + str(aux.data) + '\n'
            strg += 'Previous hash: ' + str(aux.previous_hash) + '\n'
            strg += 'Hash :' + str(aux.hash) + '\n'
            aux = aux.next
            index += 1

        return strg


# Test case 1
if __name__ == '__main__':
    blockchain = BlockChain()
    blockchain.add_block('hello')
    blockchain.add_block('world')
    blockchain.add_block('God')
    print(blockchain, sep='\n\n')  # Returns tha blocks data

print('\n------------------------------\n')
# Test case 2
blockchain = BlockChain()
blockchain.add_block()
# Cant add block without data , The block doesnt exist
print(blockchain, sep='\n\n')


print('\n------------------------------\n')
# Test case 3
blockchain = BlockChain()
blockchain.add_block()  # Cant add blok without data
blockchain.add_block('world')  # Returns the block data
blockchain.add_block('')  # Cant add block as a space str
print(blockchain, sep='\n\n')
