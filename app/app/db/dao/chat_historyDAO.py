from typing import List

from ..models.chat_history import ChatHistory


def create_chat_history(new_history :ChatHistory,session):
    session.add(new_history)
    session.commit()
    session.refresh(new_history)

def get_chat_history_by_chat_id(chat_id : int,session) ->List[ChatHistory]:
    return session.query(ChatHistory).filter(ChatHistory.chat_id == chat_id).all()