from fastapi import FastAPI
import websockets
import asyncio

app = FastAPI()


async def bithumb_ws_client():
    uri = 'wss//pubwss.bithumb.com/pub/ws'

    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(greeting)


async def test_main():
    print('')
    await bithumb_ws_client()


@app.get('/')
async def test_get():
    print('???????')
    res = await test_main()
    asyncio.run(res)
