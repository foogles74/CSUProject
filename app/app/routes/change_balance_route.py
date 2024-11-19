from fastapi import APIRouter, Body
from sqlmodel import Session
from fastapi.responses import JSONResponse

from ..db.dao.transactionDAO import create_transaction
from ..db.dao.userDAO import get_user_by_login
from ..db.database import engine
from ..db.models.transaction import Transaction

change_balance_route = APIRouter()


@change_balance_route.post('change_balance')
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
