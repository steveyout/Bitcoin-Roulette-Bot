from block_io import BlockIo
from db import db_session
from models import BitcoinBot
import messages
import json
import time
from threading import Thread

block_io = BlockIo("7d26-77f7-1dce-76e2", "justthefuckoff", 2)

def generate_for_user(user_id):
    if BitcoinBot.query.filter_by(user_id=user_id).first().user_bitcoin_address == None:
        try:
            result = block_io.get_new_address(label=user_id)
            user = BitcoinBot.query.filter_by(user_id=user_id).first()
            user.user_address_balance = 0
        except Exception as e:
            result = block_io.get_address_balance(labels=user_id)
        user = BitcoinBot.query.filter_by(user_id=user_id).first()
        address = result["data"]["balances"][0]["address"]
        user.user_bitcoin_address = address
        db_session.flush()
        return address
    else:
        user = BitcoinBot.query.filter_by(user_id=user_id).first()
        return user.user_bitcoin_address

def out_balance(address, amount, user_id):
    fee = float(block_io.get_network_fee_estimate(amounts=amount, to_addresses=address)["data"]["estimated_network_fee"])
    block_io.withdraw_from_labels(amounts=(amount-fee), from_labels="default", to_addresses=address)
    user = BitcoinBot.query.filter_by(user_id=user_id).first()
    user.user_balance -= amount/1000*0.001
    db_session.flush()

    

def update_balance():
    while (True):
        print ("Got balance", flush=True)
        result = block_io.get_my_addresses()
        for address in result["data"]["addresses"]:
            user_address = address["address"]
            amount = address["available_balance"]
            fee = float(block_io.get_network_fee_estimate(amounts=amount, to_labels="default"))
            block_io.withdraw_from_labels(amounts=(amount-fee), from_labels=user_address, to_labels="default")
            user = BitcoinBot.query.filter_by(user_bitcoin_address=user_address).first()
            user.balance += amount/0.001*1000
        time.sleep(60)
