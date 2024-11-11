from typing import List, Optional
from ..models.user import User


def get_all_users(session) -> List[User]:
    return session.query(User).all()

def get_user_by_id(id:int, session) -> Optional[User]:
    users = session.get(User, id)
    if users:
        return users
    return None

def get_user_by_email(email:str, session) -> Optional[User]:
    user = session.query(User).filter(User.email == email).first()
    if user:
        return user
    return None

def get_user_by_login(login:str, session) -> Optional[User]:
    user = session.query(User).filter(User.login == login).first()
    if user:
        return user
    return None

def create_user(new_user: User, session) -> None:
    session.add(new_user)
    session.commit()
    session.refresh(new_user)