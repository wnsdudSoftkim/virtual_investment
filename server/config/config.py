bithumb_websocket_uri = "wss://pubwss.bithumb.com/pub/ws"

binance_ticker_uri = 'https://api.binance.com/api/v3/ticker/price'

binance_symbol_uri = 'https://api.binance.com/api/v3/klines'

mongodb_service_local_uri = "mongodb://localhost:27017"


# TODO: LOCAL이 아닌 배포시엔 ENV파일로 바꾸기
class Settings:
    PROJECT_NAME = "virtual-investment"
    PROJECT_VERSION = "1.0.0"
    COLLECTION_NAME: str = "investment"
    # MONGO_SERVICE_URI = "mongodb://localhost:27017"
    MONGO_SERVICE_URI = "mongodb://flgkselql98:tjdnftkfka0501Q@investment-shard-00-00.9ea8t.mongodb.net:27017," \
                        "investment-shard-00-01.9ea8t.mongodb.net:27017," \
                        "investment-shard-00-02.9ea8t.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas" \
                        "-9s1ro9-shard-0&authSource=admin&retryWrites=true&w=majority "
    MONGO_DB = "investment"


def get_settings():
    return Settings()
