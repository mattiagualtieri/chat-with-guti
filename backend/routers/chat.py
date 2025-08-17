from fastapi import WebSocket, APIRouter, WebSocketDisconnect
from uuid import uuid1
from ..service.agent import ChatAgent


router = APIRouter(
    prefix='',
    tags=['chat']
)


@router.websocket('/chat')
async def chat(web_socket: WebSocket):
    agent = ChatAgent.instance()
    await web_socket.accept()
    session_key = str(uuid1())
    try:
        while True:
            message = await web_socket.receive_text()
            response = agent.chat(message, session_key)
            await web_socket.send_text(response)
    except WebSocketDisconnect:
        pass
