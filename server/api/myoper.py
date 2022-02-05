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
    print('??')
    pipeline=[
        {
            '$lookup': {
                'from': 'index_overview',
                'localField': '_id',
                'foreignField': 'methodology_file.en.file_name',
                'as': 'my_test'
            }
        },
        # {'$unwind': "$my_test"},
        # {
        #     '$match': {
        #         '$or': [{'_id': {'$eq': 'my_test.methodology_file.en.file_name'}}]
        #     }
        # }
        # {
        #     '$match': {
        #         '_id': 'mytest.methodology_file.en.file_id'
        #     }
        # },
        # {
        #     '$project': {
        #         '_id': 1,
        #         'field_name': 1,
        #         'mytest': 1
        #     }
        # },
    ]
    # pipeline = [
    #     {
    #         '$lookup': {
    #             'from': 'index_overview',
    #             'let': {'index_overview': '$index_overview'},
    #             'pipeline': [
    #                 {
    #                     '$match': {
    #                         '$or': ['$$index_overview.methodology_file.en','$$index_overview.methodology_file.ko','$$index_overview.factsheet_file.ko', '$$index_overview.factsheet_file.ko' ]
    #
    #                     }
    #                 }
    #             ],
    #             'as': 'match_file'
    #         }
    #     }
    # ]
    res = await op.aggregate('file',pipeline)
    print(res)
