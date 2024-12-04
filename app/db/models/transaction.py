from sqlmodel import SQLModel, Field


class Transaction(SQLModel, table=True):
    transaction_id: int = Field(default=None, primary_key=True)
    user_id : int  = Field(default=None, foreign_key="user.user_id")
    value: float