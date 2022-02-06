from fastapi import FastAPI, Depends
from api import router
from db import connect_db, close_db
from config.config import Settings, get_settings

app = FastAPI(title=get_settings().PROJECT_NAME, version=get_settings().PROJECT_VERSION)
app.include_router(router)


def open_database_connection_pool():
    connect_db()


def close_database_connection_pool():
    close_db()


@app.get('/')
async def root():
    pass


app.add_event_handler("startup", open_database_connection_pool)
app.add_event_handler("shutdown", close_database_connection_pool)
