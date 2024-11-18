from fastapi import APIRouter

signup_route = APIRouter()

@signup_route.post('/signup')
async def signup():

    return "test"