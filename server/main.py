from fastapi import FastAPI
from server.api import router
from db import connect_db, close_db
app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

app.include_router(router)


@app.get("/", include_in_schema=False)
async def root():
    return {
        "running-mode": 'development'
    }


@app.on_event("startup")
async def startup_evnet():
    connect_db()


@app.on_event('shut_down')
async def shutdown_event():
    close_db()
