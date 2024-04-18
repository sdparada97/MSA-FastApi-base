from fastapi import APIRouter
from app.log_config import logger

router = APIRouter()

@router.get("/examples/", tags=["examples"])
async def read_examples():
    logger.critical("Inicia endpoint de ejemplo con log")
    return [{"example": "data-exmaple1"}, {"example": "data-exmaple2"}]
