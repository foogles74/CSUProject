from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from routes.get_balance_route import get_balance_route
from routes.request_model_route import request_model_route
from db.database import init_db

from routes.change_balance_route import change_balance_route
from routes.signin_route import signin_route
from routes.signup_route import signup_route
from routes.home_route import home_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan = lifespan)
app.include_router(home_route)
app.include_router(signin_route)
app.include_router(signup_route)
app.include_router(change_balance_route)
app.include_router(request_model_route)
app.include_router(get_balance_route)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
