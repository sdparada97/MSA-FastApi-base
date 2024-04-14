from fastapi import APIRouter

router = APIRouter()

@router.get("/examples/", tags=["examples"])
async def read_examples():
    return [{"example": "data-exmaple1"}, {"example": "data-exmaple2"}]
