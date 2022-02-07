import random

from db.model.chart import ChartInModel
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
    symbol = ""
    await websocket.accept()
    while True:
        try:
            print('prepare send')
            receive_txt = await receive_text(websocket)

            if receive_txt.date is not '1':
                symbol = receive_txt.symbol if receive_txt.symbol is not None else symbol
                pipeline[1]['$match']['Open_time']['$gte'] = receive_txt.date
                res = await op.aggregate('b_2017', pipeline=pipeline)
                other_res = await op.get('b_2017', {'Open_time': {'$gte': receive_txt.date}}, {'trades': 1, 'Volume': 1, 'Open': 1, '_id': 0})
                result = {
                    'res': res,
                    'other_res': other_res
                }
                await websocket.send_json(result)
                print('send data')

        except Exception as exc_info:
            print('error occur: ', exc_info)
            break
    print('Disconnecting client connection')


async def receive_text(websocket: WebSocket) -> ChartInModel:
    res = await websocket.receive_json()
    model = ChartInModel(**res)
    return model
