import datetime
import hashlib
import json


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.time = datetime.datetime.utcnow()
        self.hash = self.compute_hash()

    def __repr__(self):
        from pprint import pformat
        return pformat(vars(self) , indent=4, width=1)

    def compute_hash(self):
        hash_string = self.sender + self.receiver + str(self.amount) + str(self.time)
        encoded_hash = json.dumps(hash_string, sort_keys=True).encode()
        return hashlib.sha256(encoded_hash).hexdigest()