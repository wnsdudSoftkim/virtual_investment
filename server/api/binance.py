import time
from datetime import datetime
from fastapi import APIRouter
from config.config import binance_ticker_uri, binance_symbol_uri
import requests
import pandas as pd

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
    years = list(range(2017, 2022))
    for symbol in symbols[:10]:
        for year in years:
            start_date = f'{year}-01-01'
            end_date = f'{year}-12-31'
            df = await _get_binance_data(start_date, end_date, symbols, COLUMNS)
            df.to_csv(f'C:/Users/lenovo/CoinData/{symbol[:3].lower()}_{year}_1h.csv', index=False)  # csv파일로 저장하는 부분
            time.sleep(1)


async def _get_binance_data(start_date, end_date, symbol, columns):
    data = []
    start = int(time.mktime(datetime.strptime(start_date + ' 00:00', '%Y-%m-%d %H:%M').timetuple())) * 1000
    end = int(time.mktime(datetime.strptime(end_date + ' 23:59', '%Y-%m-%d %H:%M').timetuple())) * 1000
    params = {
        'symbol': symbol,
        'interval': '1h',
        'limit': 1000,
        'startTime': start,
        'endTime': end
    }

    while start < end:
        print(datetime.fromtimestamp(start // 1000))
        params['startTime'] = start
        result = requests.get(binance_symbol_uri, params=params)
        js = result.json()
        if not js:
            break
        data.extend(js)
        start = js[-1][0] + 60000
    if not data:
        print('no data')
        return
    df = pd.DataFrame(data)
    df.columns = columns
    df['Open_time'] = df.apply(lambda x: datetime.fromtimestamp(x['Open_time'] // 1000).isoformat(), axis=1)
    df = df.drop(columns=['Close_time', 'ignore'])
    df['Symbol'] = symbol
    df.loc[:, 'Open':'tb_quote_av'] = df.loc[:, 'Open':'tb_quote_av'].astype(float)  # string to float
    df['trades'] = df['trades'].astype(int)
    return df