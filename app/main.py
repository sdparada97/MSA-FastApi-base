from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.api_router import api_router
from app.settings import settings

# Application starts
app = FastAPI(
    title=settings.PROJECT_NAME, debug=settings.DEBUG, description=settings.DESCRIPTION, version=settings.VERSION
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Welcome FastAPI Base Microservice"}
