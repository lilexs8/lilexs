from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.core import Finding
from app.schemas.core import FindingCreate

router = APIRouter(prefix="/findings", tags=["Findings"])

@router.get("")
def list_findings(db: Session = Depends(get_db)):
    return db.query(Finding).all()

@router.post("")
def create_finding(payload: FindingCreate, db: Session = Depends(get_db)):
    finding = Finding(**payload.model_dump())
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding
