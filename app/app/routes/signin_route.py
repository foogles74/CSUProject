from fastapi import APIRouter

signin_route = APIRouter()

@signin_route.post('/signin')
async def signup():
    return "test"