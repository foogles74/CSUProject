from fastapi import APIRouter, Body
from sqlmodel import Session
from fastapi.responses import JSONResponse
from app.app.db.dao.userDAO import get_user_by_email, get_user_by_login, create_user
from app.app.db.database import engine
from app.app.db.models.user import User
from app.app.tools.create_hash import create_hash

sign_in_up_route = APIRouter(tags=['User'])

@sign_in_up_route.post('/signin')
async def signin(data=Body()):
    login = data["login"]
    email = data["email"]
    password = data["password"]
    password_hash = ""
    with Session(engine) as session:
        by_email = get_user_by_email(email, session)
        by_login = get_user_by_login(login, session)
        if by_email is not None:
            if by_email.password == create_hash(password):
                password_hash = create_hash(by_email.password)
        elif by_login is not None:
            if by_login.password == create_hash(password):
                password_hash = create_hash(by_login.password)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)
        if password_hash != "":
            return JSONResponse(content={"message": "OK"}, status_code=200)
        else:
            return JSONResponse(content={"message": "Wrong password"}, status_code=401)

@sign_in_up_route.post('/signup')
async def signup(data=Body()):
    login = data["login"]
    email = data["email"]
    password = data["password"]
    with Session(engine) as session:
        if get_user_by_email(email, session) is not None:
            return JSONResponse(content={"message": "The email has already been registered"}, status_code=400)
        elif get_user_by_login(login, session) is not None:
            return JSONResponse(content={"message": "The login has already been registered"}, status_code=400)
        else:
            new_user = User(login=login, email=email, password=create_hash(password), balance=0)
            create_user(new_user, session)
    return JSONResponse(content={"message": "OK"}, status_code=200)