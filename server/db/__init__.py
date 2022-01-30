from motor.motor_asyncio import AsyncIOMotorClient
from config.config import mongodb_service_local_uri
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi.logger import logger

client: AsyncIOMotorClient = None
db = None


def connect_db():
    logger.info('connecting mongodb service')
    client = AsyncIOMotorClient(mongodb_service_local_uri)
    db = client.mydb
    collection = db.get_collection('investment')
    logger.info('complete connect')


def close_db():
    client.close()
    logger.info('close mongodb connect')


def get_mongo_db():
    return db


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
