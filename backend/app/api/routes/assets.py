from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.core import Asset
from app.schemas.core import AssetCreate

router = APIRouter(prefix="/assets", tags=["Assets"])

@router.get("")
def list_assets(db: Session = Depends(get_db)):
    return db.query(Asset).all()

@router.post("")
def create_asset(payload: AssetCreate, db: Session = Depends(get_db)):
    asset = Asset(**payload.model_dump())
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset
