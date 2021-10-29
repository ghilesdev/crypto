import hashlib


class Block:
    def __init__(self, transactions, time, index):
        self.transactions = transactions
        self.time = time
        self.index = index
        self.previous_hash = ""
        self.nonce = 0
        self.hash = self.compute_hash()

    def __repr__(self):
        from pprint import pformat
        return pformat([vars(block) for block in self.transactions], indent=4, width=1)

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
            print("\n\nTrying nonce: ", self.nonce)
            print("Obtained hash: ", self.hash)
        print("Block mined: ", self.hash)