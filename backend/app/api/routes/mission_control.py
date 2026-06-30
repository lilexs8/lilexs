from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.core import Asset, Finding, AttackPath

router = APIRouter(prefix="/mission-control", tags=["Mission Control"])

@router.get("")
def get_mission_control(organization_id: int = 1, db: Session = Depends(get_db)):
    assets = db.query(Asset).filter(Asset.organization_id == organization_id).count()
    findings = db.query(Finding).filter(Finding.organization_id == organization_id).count()
    attack_paths = db.query(AttackPath).filter(AttackPath.organization_id == organization_id).count()
    critical = db.query(Finding).filter(Finding.organization_id == organization_id, Finding.severity == "critical").count()
    high = db.query(Finding).filter(Finding.organization_id == organization_id, Finding.severity == "high").count()
    score = max(0, 100 - (critical * 10) - (high * 5) - findings)

    return {
        "security_score": score,
        "assets": assets,
        "open_findings": findings,
        "attack_paths": attack_paths,
        "critical_findings": critical,
        "lix_priority": "Focus on critical identity exposure and attack paths connected to sensitive assets."
    }
