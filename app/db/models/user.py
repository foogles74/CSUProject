from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    login : str
    password: str
    email: str
    balance : float = 0

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserSignIn(SQLModel):
    email: str
    password: str