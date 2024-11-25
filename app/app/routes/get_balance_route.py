from fastapi import APIRouter, Body
from sqlmodel import Session
from fastapi.responses import JSONResponse

from app.app.db.dao.transactionDAO import create_transaction
from app.app.db.dao.userDAO import get_user_by_login, get_user_by_email
from app.app.db.database import engine
from app.app.db.models.transaction import Transaction

get_balance_route = APIRouter()

@get_balance_route.get('/get_balance_route/{email}')
async def get_balance_routes(email : str):
    with Session(engine) as session:
        user = get_user_by_email(email, session)
        if user is not None:
            return user.balance
        else:
            return JSONResponse(content={"message": "User not found"},status_code=404)