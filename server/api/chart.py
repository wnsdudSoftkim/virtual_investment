import random

from fastapi import APIRouter, WebSocket

router = APIRouter(
    prefix='/chart',
    tags=['chart']
)


@router.websocket('/ws')
async def get_chart_endpoint(websocket: WebSocket):
    print('Accepting client connection...')
    await websocket.accept()
    while True:
        try:
            await websocket.receive_text()
            resp = {'value': random.uniform(0, 1)}
            await websocket.send_json(resp)
        except Exception as exc_info:
            print('error occur: ', exc_info)
            break
    print('Disconnecting client connection')
