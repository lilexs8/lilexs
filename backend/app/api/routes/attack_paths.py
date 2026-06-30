from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.core import AttackPath
from app.schemas.core import AttackPathCreate

router = APIRouter(prefix="/attack-paths", tags=["Attack Paths"])

@router.get("")
def list_attack_paths(db: Session = Depends(get_db)):
    return db.query(AttackPath).all()

@router.post("")
def create_attack_path(payload: AttackPathCreate, db: Session = Depends(get_db)):
    path = AttackPath(**payload.model_dump())
    db.add(path)
    db.commit()
    db.refresh(path)
    return path
