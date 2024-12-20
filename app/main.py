from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from routes.websocket_route import chat_route
from routes.request_model_route import request_model_route
from db.database import init_db
from routes.balance_route import balance_route
from routes.sign_in_up_route import sign_in_up_route



@asynccontextmanager
async def lifespan(app: FastAPI):
    # init_db()
    yield

app = FastAPI(lifespan = lifespan)
app.include_router(sign_in_up_route, prefix='/user')
app.include_router(balance_route, prefix='/balance')
app.include_router(request_model_route)
app.include_router(chat_route, prefix='/ws')


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
