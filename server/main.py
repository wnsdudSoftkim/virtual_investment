from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from server.api import router
from db import connect_db, close_db
from config.config import settings

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

app.include_router(router)


def include_router(app):
    app.include_router(router)


#
# def configure_static(app):
#     app.mount("/static", StaticFiles(directory="static"), name="static")


def open_database_connection_pool():  # new
    connect_db()


def close_database_connection_pool():
    close_db()


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    open_database_connection_pool()
    return app


@app.on_event("shutdown")
async def shutdown_event():
    close_database_connection_pool()


app = start_application()
