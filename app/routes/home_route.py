from fastapi import APIRouter

home_route = APIRouter()


@home_route.get('/')
async def home():
    return "test"
