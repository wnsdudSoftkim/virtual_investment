from typing import List
import requests
from db.data.data import SymbolData
from config.config import binance_ticker_uri


class BinanceDataManager(object):

    @classmethod
    def _get_symbol_data(cls):
        result = requests.get(binance_ticker_uri)
        js = result.json()
        symbols = [x['symbol'] for x in js]
        return symbols

    @classmethod
    def get_symbol_data(cls):
        return SymbolData.get_symbol_data()


class BinanceHandler:

    @staticmethod
    def select_symbol_top():
        return ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'ADAUSDT']

    @staticmethod
    def select_symbol_usdt() -> List[str]:
        symbols = BinanceDataManager.get_symbol_data()
        return [x for x in symbols if 'USDT' in x]

    @staticmethod
    def select_year(start: int = 2017, end: int = 2022):
        return list(range(start, end))

    @staticmethod
    def select_column(field: List = None):
        basic_field = ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'quote_av', 'trades',
                       'tb_base_av', 'tb_quote_av', 'ignore']
        return basic_field if field is None else field
