from sqlalchemy import Column, String

from db.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(autoincrement= True,type=String, nullable=False, unique=True)
    login = Column(type=String, nullable=False, unique=True)
    password = Column(type=String, nullable=False)
    email = Column(type=String, nullable=False, unique=True)