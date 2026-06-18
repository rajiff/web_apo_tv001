from fastapi import FastAPI
from app.api import hello_world

app = FastAPI(title="Web Apo API")

app.include_router(hello_world.router)

@app.get("/", tags=["root"])
async def read_root() -> dict[str, str]:
    return {"message": "Welcome to Web Apo"}
