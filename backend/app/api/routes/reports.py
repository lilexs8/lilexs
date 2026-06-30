from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.core import Report
from app.schemas.core import ReportCreate

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("")
def list_reports(db: Session = Depends(get_db)):
    return db.query(Report).all()

@router.post("")
def create_report(payload: ReportCreate, db: Session = Depends(get_db)):
    report = Report(**payload.model_dump())
    db.add(report)
    db.commit()
    db.refresh(report)
    return report
