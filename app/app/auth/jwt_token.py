import time
from datetime import datetime
from fastapi import HTTPException, status
from jose import jwt, JWTError

from app.app.db.settings import get_settings

settings = get_settings()
SECRET_KEY = settings.SECRET_KEY

def create_access_token(user: str) -> str:
    payload = {
    "user": user,
    "expires": time.time() + 36000
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_access_token(token: str) -> bool:
    try:
        data = jwt.decode(token, SECRET_KEY,
        algorithms=["HS256"])
        expire = data.get("expires")
        if expire is None:
            return False
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            return False
        return True
    except JWTError:
        return False
