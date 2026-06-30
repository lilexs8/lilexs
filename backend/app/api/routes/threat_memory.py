from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.core import ThreatMemory
from app.schemas.core import ThreatMemoryCreate

router = APIRouter(prefix="/threat-memory", tags=["Threat Memory"])

@router.get("")
def list_memory(db: Session = Depends(get_db)):
    return db.query(ThreatMemory).all()

@router.post("")
def create_memory(payload: ThreatMemoryCreate, db: Session = Depends(get_db)):
    memory = ThreatMemory(**payload.model_dump())
    db.add(memory)
    db.commit()
    db.refresh(memory)
    return memory
