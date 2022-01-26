import motor.motor_asyncio
from config.config import mongodb_service_local_uri
from pydantic import BaseModel, Field
from bson import ObjectId

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_service_local_uri)
database = client.mydb
collection = database.get_collection('investment')


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
