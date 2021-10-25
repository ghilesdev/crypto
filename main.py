import datetime
import time
import pprint
import blockchain

pp = pprint.PrettyPrinter(indent=4)
def main():
    transactions = []
    bc = blockchain.BlockChain()
    bc.add_transaction("michael", "jim", 1)
    bc.mine_pending_transactions()
    # block_one = blockchain.Block(transactions=transactions, time=datetime.datetime.utcnow(), index=1)
    # bc.add_block(block_one)
    #
    # block_two = blockchain.Block(transactions=transactions, time=datetime.datetime.utcnow(), index=2)
    # bc.add_block(block_two)
    #
    # block_three = blockchain.Block(transactions=transactions, time=datetime.datetime.utcnow(), index=3)
    # bc.add_block(block_three)

    pp.pprint(bc)


if __name__ == '__main__':
    main()