from datetime import datetime
from typing import Optional, List, Any

from pydantic import BaseModel


class PriceTradeVolumeModel(BaseModel):
    trades: int
    Volume: float
    Open: int

    def __init__(self, **data: Any):
        if 'Open' in data:
            data['Open'] = round(data.get('Open') * 1195.73)
        super().__init__(**data)


class PriceModel(BaseModel):
    x: Optional[str]
    y: Optional[str]


class PriceListModel(PriceModel):
    result: List[PriceModel]


class PriceOutModel(PriceListModel, PriceTradeVolumeModel):
    res: PriceListModel
    other_res: PriceTradeVolumeModel


class ChartInModel(BaseModel):
    price: Optional[str]
    date: str
    symbol: Optional[str]
