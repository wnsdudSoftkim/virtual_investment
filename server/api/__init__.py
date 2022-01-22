from fastapi import APIRouter
from api.bithumb import router as bithumb_router
from api.binance import router as binance_router
router = APIRouter()

router.include_router(bithumb_router)
router.include_router(binance_router)