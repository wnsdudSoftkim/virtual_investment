from db import get_mongo_db
from config.config import Settings


class Operator(object):

    @staticmethod
    async def get(condition: dict, projection: dict):
        db = get_mongo_db()
        collection = Settings.COLLECTION_NAME
        if condition is None:
            condition = {}

        print(db[collection])
        return await db[collection].find_one(condition, projection)

    @staticmethod
    async def update(condition: dict, field: dict):
        db = get_mongo_db()
        collection = Settings.COLLECTION_NAME

        if condition is None:
            condition = {}
        if len(field) == 0:
            return 0
        await db[collection].update_one(condition, field)
        return condition.get('_id')

    @staticmethod
    async def create(field: dict):
        db = get_mongo_db()
        collection = Settings.COLLECTION_NAME

        if len(field) == 0:
            return 0
        await db[collection].insert_one(field)
        return field.get('_id')

    @staticmethod
    async def delete(condition: dict):
        db = get_mongo_db()
        collection = Settings.COLLECTION_NAME

        await db[collection].delete_one(condition)
        return condition.get('_id')
