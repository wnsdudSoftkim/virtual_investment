from fastapi import APIRouter
from db.operations import Operator as op

router = APIRouter(
    prefix='/operator',
    tags=['operator']
)


@router.get('/my-operator')
async def sample_router():
    print('??')
    res = await op.get({}, {})
    print(res)
