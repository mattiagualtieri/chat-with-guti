import logging
from fastapi import Response, WebSocket, APIRouter, WebSocketDisconnect
from uuid import uuid1
from ..service.agent import ChatAgent


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)


router = APIRouter(
    prefix='',
    tags=['chat']
)


@router.get('/health')
async def health():
    logging.info('Called /health')
    return Response()


@router.websocket('/chat')
async def chat(web_socket: WebSocket):
    agent = ChatAgent.instance()
    await web_socket.accept()
    session_key = str(uuid1())
    try:
        while True:
            message = await web_socket.receive_text()
            logging.info(f'Received message: {message}')
            response = agent.chat(message, session_key)
            await web_socket.send_text(response)
    except WebSocketDisconnect:
        pass
