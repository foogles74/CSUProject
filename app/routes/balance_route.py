from fastapi import APIRouter, Body
from sqlmodel import Session
from fastapi.responses import JSONResponse

from app.db.dao.transactionDAO import create_transaction
from app.db.dao.userDAO import get_user_by_login, get_user_by_email
from app.db.database import engine
from app.db.models.transaction import Transaction

balance_route = APIRouter(tags=['Balance'])


@balance_route.post('/change_balance')
async def home(data=Body()):
    login = data["login"]
    value = data["value"]
    with Session(engine) as session:
        user = get_user_by_login(login, session)
        if user is not None:
            new_transaction = Transaction(user_id=user.user_id, value=value)
            create_transaction(new_transaction, session)
            return JSONResponse(content={"message": "OK"}, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)

@balance_route.get('/get_balance_route/{email}')
async def get_balance_routes(email : str):
    with Session(engine) as session:
        user = get_user_by_email(email, session)
        if user is not None:
            return user.balance
        else:
            return JSONResponse(content={"message": "User not found"},status_code=404)
