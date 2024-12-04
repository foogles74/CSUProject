from sqlmodel import SQLModel, Field


class Chat(SQLModel, table=True):
    chat_id: int = Field(default=None, primary_key=True)
    user_id : int  = Field(default=None, foreign_key="user.user_id")
    name: str