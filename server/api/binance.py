import time
from datetime import datetime
from fastapi import APIRouter
from config.config import binance_ticker_uri
import requests

router = APIRouter(
    prefix='/binance',
    tags=['binance']
)


@router.get('/previous-data')
async def get_previous_data():
    result = requests.get(binance_ticker_uri)
    js = result.json()
    symbols = [x['symbol'] for x in js]
    symbols_usdit = [x for x in symbols if 'USDT' in x]
    COLUMNS = ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'quote_av', 'trades',
               'tb_base_av', 'tb_quote_av', 'ignore']

    start_date = '2021-06-01'
    end_date = '2021-12-31'
    symbols = symbols_usdit[0]
    await _get_binance_data(start_date, end_date, symbols)


async def _get_binance_data(start_date, end_date, symbol):
    data = []
    start = int(time.mktime(datetime.strptime(start_date + ' 00:00', '%Y-%m-%d %H:%M').timetuple())) * 1000
    end = int(time.mktime(datetime.strptime(end_date + ' 23:59', '%Y-%m-%d %H:%M').timetuple())) * 1000
    params = {
        'symbol': symbol,
        'interval': '1m',
        'limit': 1000,
        'startTime': start,
        'endTime': end
    }

    while start < end:
        print(datetime.fromtimestamp(start // 1000))
        params['startTime'] = start
        result = requests.get(binance_ticker_uri, params=params)
        js = result.json()
        if not js:
            break
