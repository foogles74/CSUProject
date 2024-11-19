from fastapi import APIRouter

from ..models.qwen.qwem_model import QwenModel

request_model_route = APIRouter()


@request_model_route.post('/request_model')
async def signup(text):
    model = QwenModel()
    generated_text = model.generate_text(text)
    return generated_text