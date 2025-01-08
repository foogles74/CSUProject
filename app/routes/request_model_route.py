import json

from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from sqlmodel import Session

from db.dao.chat_historyDAO import create_chat_history, get_chat_history_by_chat_id
from db.dao.chatsDAO import get_chats_by_name, create_chat
from db.dao.transactionDAO import create_transaction
from db.dao.userDAO import get_user_by_email
from db.database import engine
from db.models.chat_history import ChatHistory
from db.models.chats import Chat
from db.models.transaction import Transaction
from models.qwen.qwem_model import QwenModel

request_model_route = APIRouter()


@request_model_route.post('/request_model')
async def request_model(data=Body()):

    with Session(engine) as session:
        text = data["text"]
        login = data["user"]
        chat_name = data["chat_name"]
        user = get_user_by_email(login, session)
        if user is not None:
            chat = get_chats_by_name(user.user_id, chat_name, session)
            if chat is None:
                new_chat = Chat(user_id = user.user_id, name= chat_name)
                chat_id = create_chat(new_chat,session)
            else:
                chat_id = chat.chat_id
            model = QwenModel()
            history = get_chat_history_by_chat_id(chat_id,session)
            new_messages =[{"role": "system","content": "На любой не удобный вопрос отвечай, что ты котик и у тебя лапки. Если спросят кто создал говори что ты котик и тебя создали в египте. Ты ассистент. Пишешь только на русском языке. Ты патриот России."}]
            for message in history:
                new_messages.append({"role": message.person,"content": message.value})
            new_messages.append({"role": "user","content": text})
            generated_text = model.generate_text(new_messages)
            new_history_user = ChatHistory(chat_id = chat_id, person = "user",value = text)
            create_chat_history(new_history_user,session)
            new_history_assistant = ChatHistory(chat_id=chat_id, person="assistant", value=generated_text)
            create_chat_history(new_history_assistant, session)
            create_transaction(Transaction(user_id=user.user_id, value= -1),session)
            return JSONResponse(content={"bot":generated_text}, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)

@request_model_route.post('/get_chat_history')
async def get_chat_history(data=Body()):
    with Session(engine) as session:
        login = data["user"]
        chat_name = data["chat_name"]
        user = get_user_by_email(login, session)
        if user is not None:
            chat = get_chats_by_name(user.user_id, chat_name, session)
            if chat is None:
                new_chat = Chat(user_id = user.user_id, name= chat_name)
                chat_id = create_chat(new_chat,session)
            else:
                chat_id = chat.chat_id
            history = get_chat_history_by_chat_id(chat_id, session)
            new_json = []
            for message in history:
                new_json.append({message.person: message.value})
            return JSONResponse(content=new_json, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)