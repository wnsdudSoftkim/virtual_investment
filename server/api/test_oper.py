from fastapi import APIRouter

from db.operations import Operator as op

router = APIRouter(
    prefix='/operator',
    tags=['operator']
)


@router.get('/index-oper')
async def sample_oper():
    pipeline = [
        {
            '$match': {'Open_time': {'$gte': "2017-08-18 10:03:46.000Z"}}
        }, {
            '$limit': 1000
        }
    ]
    res = await op.aggregate('b_2017', pipeline=pipeline)
