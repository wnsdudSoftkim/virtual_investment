import random
from db.operations import Operator as op
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
            print('test1')
            await websocket.receive_text()
            print('test2')
            resp = {'value': random.uniform(0, 1)}
            await websocket.send_json(resp)
        except Exception as exc_info:
            print('error occur: ', exc_info)
            break
    print('Disconnecting client connection')
