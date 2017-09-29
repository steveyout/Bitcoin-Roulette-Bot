from db import Base
from sqlalchemy import Column, Integer, String, Float

class BitcoinBot(Base):
    __tablename__ = "bitcoin_bot"
    idbitcoin_bot = Column(Integer, primary_key = True, nullable=False)
    user_id = Column(String(45))
    user_balance = Column(Float)
    user_bet = Column(String(10))
    user_chat_id = Column(Integer)
    user_bet_size = Column(Integer)
    user_bitcoin_address = Column(String(1000))
    user_refferal_address = Column(String(45))

    def __init__(self, user_id, user_balance, user_bet, user_chat_id, user_refferal_address=None):
        self.user_balance = user_balance
        self.user_id = user_id
        self.user_bet = user_bet
        self.user_chat_id = user_chat_id
        self.user_refferal_address = user_refferal_address