from fastapi import FastAPI
import websockets
import asyncio

app = FastAPI()


async def bithumb_ws_client():
    uri = 'wss//pubwss.bithumb.com/pub/ws'

    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(greeting)


async def main():
    print('?')
    await bithumb_ws_client()


@app.get('/')
async def test_get():
    print('???????')
    asyncio.run(main())


if __name__ == "__main__":
    app.run(debug=True)
