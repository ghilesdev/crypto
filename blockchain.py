import datetime
import hashlib
import json
import time


class BlockChain:
    def __init__(self):
        self.chain = []

    def __repr__(self):
        from pprint import pformat
        return pformat([vars(block) for block in self.chain], indent=4, width=1)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        if len(self.chain)>0:
            block.previous_hash = self.get_last_block().hash
        else:
            block.previous_hash = "none"
        self.chain.append(block)

class Block:
    def __init__(self, transactions, time, index):
        self.transactions = transactions
        self.time = time
        self.index = index
        self.previous_hash = ""
        self.hash = self.compute_hash()

    def compute_hash(self):
        transactions_hash = "".join(
            transaction.hash for transaction in self.transactions
        )
        hash_string = transactions_hash + self.previous_hash + str(self.index) + str(self.time)
        encoded_hash = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(encoded_hash).hexdigest()


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