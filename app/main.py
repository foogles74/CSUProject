import time
from contextlib import asynccontextmanager
import uvicorn
from api_analytics.fastapi import Analytics
from fastapi import FastAPI

from tools.rebbit import send_log
from models.qwen.qwem_model import QwenModel
from routes.websocket_route import chat_route
from routes.request_model_route import request_model_route
from db.database import init_db
from db.settings import get_settings
from routes.balance_route import balance_route
from routes.sign_in_up_route import sign_in_up_route



@asynccontextmanager
async def lifespan(app: FastAPI):
    # init_db()
    yield

app = FastAPI(lifespan = lifespan)
app.add_middleware(Analytics, api_key=get_settings().FAST)
app.include_router(sign_in_up_route, prefix='/user')
app.include_router(balance_route, prefix='/balance')
app.include_router(request_model_route)
app.include_router(chat_route, prefix='/ws')


if __name__ == "__main__":
    time.sleep(3)
    send_log("Логирование Запущено")
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
