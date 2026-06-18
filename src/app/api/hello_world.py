from fastapi import APIRouter

router = APIRouter()

@router.get("/hello", tags=["basic"])
async def hello_world() -> dict[str, str]:
    return {"message": "Hello World"}
