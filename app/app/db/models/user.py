from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    login : str
    password: str
    email: str
    balance : float = 0