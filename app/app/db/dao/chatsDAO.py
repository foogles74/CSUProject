from typing import List, Optional
from ..models.chats import Chat

def get_all_chats(session)-> List[Chat]:
    return session.query(Chat).all()

def get_chats_by_user(user_id:int,session)-> List[Chat]:
    chats = session.get(Chat, user_id)
    if chats:
        return chats
    return []

def get_chats_by_name(user_id:int, name : str, session)-> Optional[Chat]:
    chat = session.get(Chat, user_id, name)
    if chat:
        return chat
    return None

def create_chat(new_chat: Chat, session) -> None:
    session.add(new_chat)
    session.commit()
    session.refresh(new_chat)