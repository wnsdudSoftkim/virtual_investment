from fastapi import APIRouter

from db.model.myoper import IndexModel
from db.operations import Operator as op

router = APIRouter(
    prefix='/operator',
    tags=['operator']
)


@router.get('/my-operator')
async def sample_router():
    print('??')
    # field = {
    #     'name': 'sample',
    #     'methodology_file': {
    #         'en': 'asc',
    #         'ko': 'asc'
    #     },
    #     'factsheet_file': {
    #         'en': 'asc',
    #         'ko': 'asc'
    #     }
    #
    # }
    field = {
        'field_name': 'jun2',
        'field_type': 'test2'
    }
    model = IndexModel(**field)
    res = await op.create('file', field)
    print(res)

@router.get('/index-oper')
async def sample_oper():
   res = await op.get('b_2017', {'Open_time':''})
