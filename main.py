import datetime
import time
import pprint
import blockchain

pp = pprint.PrettyPrinter(indent=4)
def main():
    bc = blockchain.BlockChain()
    bc.add_transaction("michael", "jim", 1)
    bc.mine_pending_transactions(miner="Aghiles")

    pp.pprint(bc)


if __name__ == '__main__':
    main()