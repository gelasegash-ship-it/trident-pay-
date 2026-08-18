from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
class UserLogin(BaseModel): email: str; password: str
@router.post("/login")
def login(user: UserLogin): return {"access_token": "fake_token_trident", "token_type": "bearer"}
