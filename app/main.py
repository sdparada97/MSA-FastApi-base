from fastapi import FastAPI

from app.routes import examples

# Application starts
app = FastAPI(
    title="Microservice Template",
)

# Include routers
app.include_router(examples.router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Welcome FastAPI Base Microservice"}
