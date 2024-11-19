from fastapi import APIRouter, Body
from sqlmodel import Session
from fastapi.responses import JSONResponse

from ..db.dao.userDAO import get_user_by_email, get_user_by_login, create_user
from ..db.database import engine
from ..db.models.user import User
from ..tools.create_hash import create_hash

signup_route = APIRouter()


@signup_route.post('/signup')
async def signup(data=Body()):
    login = data["login"]
    email = data["email"]
    password = data["password"]
    with Session(engine) as session:
        if get_user_by_email(email,session) == None:
            return JSONResponse(content={"message": "The email has already been registered"}, status_code=400)
        elif get_user_by_login(login,session) == None:
            return JSONResponse(content={"message": "The login has already been registered"}, status_code=400)
        else:
            new_user = User(login=login, email=email, password=create_hash(password), balance=0)
            create_user(new_user, session)
    return JSONResponse(content={"message": "OK"}, status_code=200)
