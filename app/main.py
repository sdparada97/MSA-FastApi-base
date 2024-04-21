from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import examples

# Application starts
app = FastAPI(title="Microservice Template", debug=True)

app.include_router(examples.router, prefix="/api")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=3600,
)


@app.get("/")
async def root():
    return {"message": "Welcome FastAPI Base Microservice"}
