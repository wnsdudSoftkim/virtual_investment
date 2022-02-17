from fastapi import APIRouter

from db.model.chart import IndexModel
from db.operations import Operator as op

router = APIRouter(
    prefix='/operator',
    tags=['operator']
)


@router.get('/my-operator')
async def sample_router():
    field = {
        'field_name': 'jun2',
        'field_type': 'test2'
    }
    model = IndexModel(**field)
    res = await op.create('file', field)


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
