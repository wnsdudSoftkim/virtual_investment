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
    project = {'_id': 0, 'Close': 0, 'High': 0, 'Low': 0, 'Volume': 0, 'Open': 0, 'Open_time': 0, 'Symbol': 0,
               'quote_av': 0, 'tb_base_av': 0, 'tb_quote_av': 0, 'trades': 0}
    pipeline = [
        {
            '$addFields': {
                'x': '$Open_time',
                'y': '$Open'
            }
        },
        {
            '$match': {'Open_time': {'$gte': "2017-08-17 10:03:46.000Z"}}
        }, {
            '$limit': 30
        }, {
            '$project': project
        },

    ]

    await websocket.accept()
    while True:
        try:
            print('prepare send')
            receive_txt = await websocket.receive_text()
            print(receive_txt)
            if receive_txt == '1':
                pass
            else:
                pipeline[1]['$match']['Open_time']['$gte'] = receive_txt
                res = await op.aggregate('b_2017', pipeline=pipeline)
                await websocket.send_json(res)
                print('resend complete')
        except Exception as exc_info:
            print('error occur: ', exc_info)
            break
    print('Disconnecting client connection')
