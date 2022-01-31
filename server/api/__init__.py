from fastapi import APIRouter
from api.bithumb import router as bithumb_router
from api.binance import router as binance_router
from api.myoper import router as operator_router
from api.chart import router as chart_router
router = APIRouter()

router.include_router(bithumb_router)
router.include_router(binance_router)
router.include_router(operator_router)
router.include_router(chart_router)
