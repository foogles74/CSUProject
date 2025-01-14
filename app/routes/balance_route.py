from fastapi import APIRouter, Body
from sqlmodel import Session
from fastapi.responses import JSONResponse

from db.dao.transactionDAO import create_transaction
from db.dao.userDAO import get_user_by_login, get_user_by_email
from db.database import engine
from db.models.transaction import Transaction

from tools.rebbit import send_log

balance_route = APIRouter(tags=['Balance'])


@balance_route.post('/change_balance')
async def home(data=Body()):
    login = data["login"]
    value = data["value"]
    with Session(engine) as session:
        user = get_user_by_email(login, session)
        if user is not None:
            new_transaction = Transaction(user_id=user.user_id, value=value)
            create_transaction(new_transaction, session)
            return JSONResponse(content={"message": "OK"}, status_code=200)
        else:
            send_log(f"Пользователь {data["email"]} сломалось изменение баланса")
            return JSONResponse(content={"message": "User not found"}, status_code=400)

@balance_route.post('/get_balance_route')
async def get_balance_routes(data=Body()):
    email = data["email"]
    with Session(engine) as session:
        user = get_user_by_email(email, session)
        if user is not None:
            return JSONResponse(content={"balance": str(user.balance)},status_code=200)
        else:
            send_log(f"Пользователь {data["email"]} сломалось get_balance_routes")
            return JSONResponse(content={"message": "User not found"},status_code=404)
