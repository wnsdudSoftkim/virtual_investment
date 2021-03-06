import json

from fastapi import APIRouter, WebSocket

from db.model.chart import ChartInModel
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
            receive_txt = await receive_text(websocket)
            if receive_txt.date != '1':
                year = receive_txt.date[:4]
                date = cm.calculate_date(receive_txt.date)
                symbol = receive_txt.symbol if receive_txt.symbol is not None else symbol
                pipeline[1]['$match']['Open_time']['$gte'] = date
                condition = cm.change_date(date)
                result = await cm.get_chart_data(year, symbol, pipeline, condition, project)
                await websocket.send_json(result)

        except Exception as exc_info:
            print('error occur: ', exc_info)
            break
    print('Disconnecting client connection')


async def receive_text(websocket: WebSocket) -> ChartInModel:
    res = await websocket.receive_json()
    model = ChartInModel(**res)
    return model
