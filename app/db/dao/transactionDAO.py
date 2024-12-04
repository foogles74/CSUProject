from typing import List, Optional
from .userDAO import change_balance
from ..models.transaction import Transaction


def get_all_transactions(session) -> List[Transaction]:
    return session.query(Transaction).all()

def create_transaction(new_transaction : Transaction,session):
    session.add(new_transaction)
    session.commit()
    session.refresh(new_transaction)
    change_balance(new_transaction.user_id, new_transaction.value,session)

def get_history_transactions(user_id,session) -> List[Transaction]:
    return session.query(Transaction).filter(Transaction.user_id == user_id).all()