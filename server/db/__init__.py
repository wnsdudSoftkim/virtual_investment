import certifi
import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
from config.config import mongodb_service_local_uri, Settings
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi.logger import logger
from typing import Optional


class Database:
    client = None
    db = None


database = Database()


def connect_db():
    # print('connecting mongodb service')
    logger.info('connecting mongodb service')
    database.client = AsyncIOMotorClient(Settings.MONGO_SERVICE_URI, tlsCAFile=certifi.where())
    database.db = database.client[Settings.MONGO_DB]
    logger.info('complete connect')


def close_db():
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


class BaseMongoDBModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
