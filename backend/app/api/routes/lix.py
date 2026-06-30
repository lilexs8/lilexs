from fastapi import APIRouter
from app.schemas.core import LixRequest
from app.services.lix import ask_lix

router = APIRouter(prefix="/lix", tags=["Lix"])

@router.post("/chat")
def chat(payload: LixRequest):
    return ask_lix(payload.question, payload.context)
