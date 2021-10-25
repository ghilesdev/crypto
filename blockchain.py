import datetime
import hashlib
import json
import time


class BlockChain:
    def __init__(self):
        self.chain = [self.add_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 5
        self.block_size = 10

    def __repr__(self):
        from pprint import pformat
        return pformat([vars(block) for block in self.chain], indent=4, width=1)

    def add_genesis_block(self):
        transactions = [Transaction("me", "you", 10)]
        block = Block(transactions, datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"), 1)
        block.previous_hash = "None"
        return block

    def mine_pending_transactions(self):
        transactions_nbr = len(self.pending_transactions)
        if transactions_nbr < 1:
            raise ValueError("must be at least one pending transaction")

        for i in range(0, transactions_nbr, self.block_size):
            end = i + self.block_size
            if i > transactions_nbr:
                end = transactions_nbr

            transactions_slice = self.pending_transactions[i:end]
            block = Block(transactions_slice, datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"), len(self.chain))
            last_hash = self.get_last_block().hash
            block.previous_hash = last_hash
            block.mine(self.difficulty)
            self.chain.append(block)
        print("Mining success !")

    def add_transaction(self, sender, receiver, amount):
        transaction = Transaction(sender, receiver, amount)
        self.pending_transactions.append(transaction)

    def add_block(self, block):
        if len(self.chain)>0:
            block.previous_hash = self.get_last_block().hash
        else:
            block.previous_hash = "none"
        self.chain.append(block)

    def get_last_block(self):
        return self.chain[-1]

class Block:
    def __init__(self, transactions, time, index):
        self.transactions = transactions
        self.time = time
        self.index = index
        self.previous_hash = ""
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        transactions_hash = "".join(
            transaction.hash for transaction in self.transactions
        )
        hash_string = str(self.time) + transactions_hash + self.previous_hash + str(self.index) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def mine(self, difficulty):
        string_to_mine = ''.join(str(char) for char in list(range(difficulty)))

        while self.hash[0:difficulty] != string_to_mine:
            self.nonce += 1
            self.hash = self.compute_hash()
        print("Block mined: ", self.hash)


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = datetime.datetime.utcnow()
        self.hash = self.compute_hash()

    def compute_hash(self):
        hash_string = self.sender + self.receiver + str(self.amount) + str(self.time)
        encoded_hash = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(encoded_hash).hexdigest()