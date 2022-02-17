from typing import List, Dict, Any
from db.operations import Operator as op


class ChartManager(object):

    @classmethod
    async def get_chart_data(cls, year: str, symbol: str, pipeline: List[Dict[str, Any]],
                             condition: Dict[str, Any], project: Dict[str, int]):
        res = await cls._get_price_data(year, symbol, pipeline)
        other_res = await cls._get_trades_data(year, symbol, condition, project)
        return {
            'res': res,
            'other_res': other_res
        }

    @classmethod
    async def _get_price_data(cls, year: str, symbol: str, pipeline: List[Dict[str, Any]]):
        return await op.aggregate(f'{symbol[0].lower()}_{year}', pipeline=pipeline)

    @classmethod
    async def _get_trades_data(cls, year: str, symbol: str, condition: Dict[str, Any], project: Dict[str, int]):
        return await op.get(f'{symbol[0].lower()}_{year}', condition, project)

    @classmethod
    def change_date(cls, date: str):
        return {'Open_time': {'$gte': date}}

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


class ChartHourHanlder:
    """TODO
        send 1h, 30m select data
    """
    # @classmethod
    # async def _get_trades_hour_data(cls, year: str, symbol: str, condition: Dict[str, Any], project: Dict[str, int]):
    #     return await op.get(f'{symbol[0].lower()}_{year}', condition, project)
