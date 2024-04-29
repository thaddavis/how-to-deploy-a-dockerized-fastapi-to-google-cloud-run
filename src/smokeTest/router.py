from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ResponseBody(BaseModel):
    message: str

@router.get("/hello-world")
def prompt() -> ResponseBody:
    return {"message": "Hello, world!"}