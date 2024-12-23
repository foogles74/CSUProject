from fastapi import WebSocket, APIRouter


chat_route = APIRouter()

@chat_route.websocket("/messages")
async def websocket_endpoint(websocket: WebSocket):
    print("connected open websocket")
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"{data}")