import random

from db.model.chart import ChartInModel
from db.operations import Operator as op
from fastapi import APIRouter, WebSocket

from logic.chart import ChartManager as cm

router = APIRouter(
    prefix='/chart',
    tags=['chart']
)


@router.websocket('/ws')
async def get_chart_endpoint(websocket: WebSocket):
    print('Accepting client connection...')
    pipeline = cm.get_pipeline()

    project = {'trades': 1, 'Volume': 1, 'Open': 1, '_id': 0}
    symbol = ""
    await websocket.accept()
    while True:
        try:
            print('prepare send')
            receive_txt = await receive_text(websocket)
            if receive_txt.date is not '1':
                year = receive_txt.date[:4]
                symbol = receive_txt.symbol if receive_txt.symbol is not None else symbol
                pipeline[1]['$match']['Open_time']['$gte'] = receive_txt.date
                condition = cm.change_date(year)
                result = await cm.get_chart_data(year, symbol, pipeline, condition, project)

                await websocket.send_json(result)
                print('send data')

        except Exception as exc_info:
            print('error occur: ', exc_info)
            break
    print('Disconnecting client connection')


async def receive_text(websocket: WebSocket) -> ChartInModel:
    res = await websocket.receive_json()
    print(res)
    model = ChartInModel(**res)
    return model
