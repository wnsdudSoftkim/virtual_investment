from fastapi import FastAPI
from server.api import router

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

app.include_router(router)


@app.get("/", include_in_schema=False)
async def root():
    return {
        "running-mode": 'development'
    }
