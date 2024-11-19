from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from routes.change_balance_route import change_balance_route
from routes.signin_route import signin_route
from routes.signup_route import signup_route
from routes.home_route import home_route
from sqlmodel import Session
from db.models.user import User
from db.dao.userDAO import create_user
from db.database import init_db, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan = lifespan)

app.include_router(home_route)
app.include_router(signin_route)
app.include_router(signup_route)
app.include_router(change_balance_route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
    user_admin = User(login = "admin",email="admin@admin", password="123qwe",balance=999999)
    with Session(engine) as session:
        create_user(user_admin,session)