from db import get_mongo_db
from config.config import Settings


class Operator(object):
    collection = Settings.COLLECTION_NAME

    async def get(self, condition: dict, projection: dict):
        db = get_mongo_db()
        if isinstance(projection, list) and len(projection) > 0:
            projection = {field: 1 for field in projection}
        return await db[self.collection].find_one(condition, projection)

    async def update(self, condition: dict, field: dict):
        db = get_mongo_db()
        if condition is None:
            condition = {}
        if len(field) == 0:
            return 0
        await db[self.collection].update_one(condition, field)
        return condition.get('_id')

    async def create(self, field: dict):
        db = get_mongo_db()
        if len(field) == 0:
            return 0
        await db[self.collection].insert_one(field)
        return field.get('_id')

    async def delete(self, condition: dict):
        db = get_mongo_db()
        await db[self.collection].delete_one(condition)
        return condition.get('_id')
