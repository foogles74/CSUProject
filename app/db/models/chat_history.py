from sqlmodel import SQLModel, Field


class ChatHistory(SQLModel, table=True):
    chat_history_id: int = Field(default=None, primary_key=True)
    chat_id : int  = Field(default=None, foreign_key="chat.chat_id")
    person: str
    value : str