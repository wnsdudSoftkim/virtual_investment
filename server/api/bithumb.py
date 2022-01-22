import websockets
import json
from config import config
from fastapi import APIRouter

router = APIRouter(
    prefix='/bithumb',
    tags=['bithumbs']
)

# real-time data
@router.get('/get-client')
async def bithumb_ws_client():
    uri = config.bithumb_websocket_uri

    async with websockets.connect(uri, ping_interval=None) as websocket:
        res = await websocket.recv()
        print(res)

        subscribe_fmt = {
            'type': 'ticker',
            'symbols': ['BTC_KRW'],
            'tickTypes': ['1H']
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)
