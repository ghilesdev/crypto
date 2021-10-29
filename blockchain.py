import datetime

from block import Block
from transaction import Transaction


class BlockChain:
    def __init__(self):
        self.chain = [self.add_genesis_block()]
        self.pending_transactions = []
        self.difficulty = 3
        self.block_size = 10
        self.miner_reward = 10

    def __repr__(self):
        from pprint import pformat
        return pformat([vars(block) for block in self.chain], indent=4, width=1)

    def add_genesis_block(self):
        """Creates first block"""
        transactions = [Transaction("me", "you", 10)]
        block = Block(transactions, datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"), 1)
        block.previous_hash = "None"
        return block

    def mine_pending_transactions(self, miner=""):
        """Tries to solve PoW algorithm to validate transactions and add blocks to the chain."""
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
        reward = Transaction("Miner reward", miner, self.miner_reward)
        self.pending_transactions.append(reward)

    def add_transaction(self, sender, receiver, amount):
        transaction = Transaction(sender, receiver, amount)
        self.pending_transactions.append(transaction)

    def get_last_block(self):
        return self.chain[-1]


