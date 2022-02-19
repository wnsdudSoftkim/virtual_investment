import json
from datetime import datetime
from typing import List, Dict, Any, Union

from db.model.chart import PriceTradeVolumeModel
from db.operations import Operator as op


class ChartManager(object):

    @classmethod
    async def get_chart_data(cls, year: str, symbol: str, pipeline: List[Dict[str, Any]],
                             condition: Dict[str, Any], project: Dict[str, int]):
        res = await cls._get_price_data(year, symbol, pipeline)
        other_res = await cls._get_trades_data(year, symbol, condition, project)
        result = {'res': res, 'other_res': other_res.dict()}

        return result

    @classmethod
    async def _get_price_data(cls, year: str, symbol: str, pipeline: List[Dict[str, Any]]):
        res = await op.aggregate(f'{symbol.lower()}_{year}_30m', pipeline=pipeline)
        for doc in res:
            doc['x'] = datetime.strptime(doc.get('x'), "%Y-%m-%dT%H:%M:%S").strftime('%Y-%m-%d/%H:%M')
            doc['y'] = round(doc.get('y') * 1195.73)
        return res

    @classmethod
    async def _get_trades_data(cls, year: str, symbol: str, condition: Dict[str, Any], project: Dict[str, int]) \
            -> PriceTradeVolumeModel:
        res = await op.get(f'{symbol.lower()}_{year}_1h', condition, project)
        return PriceTradeVolumeModel(**res)

    @classmethod
    def change_date(cls, date: str):
        return {'Open_time': {'$gte': date}}

    @classmethod
    def calculate_date(cls, date: str):
        return f'{date[:4]}-{date[5:10]}T{date[11:16]}'

    @classmethod
    def get_pipeline(cls):
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
        return pipeline
