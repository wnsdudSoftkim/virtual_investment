from motor.motor_asyncio import AsyncIOMotorClient
from config.config import mongodb_service_local_uri, Settings
from pydantic import BaseModel, Field
from bson import ObjectId
import logging


class Database:
    client = None
    db = None


database = Database()


def connect_db():
    print('connecting mongodb service')
    logger = logging.getLogger("base_middleware")
    logger.setLevel(logging.INFO)
    logger.info('connecting mongodb service')
    database.client = AsyncIOMotorClient(Settings.MONGO_SERVICE_URI)
    database.db = database.client[Settings.MONGO_DB]
    logger.info('complete connect')


def close_db():
    logger = logging.getLogger("base_middleware")
    logger.setLevel(logging.INFO)
    database.client.close()
    logger.info('close mongodb connect')


def get_mongo_db():
    return database.db

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
