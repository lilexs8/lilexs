from pydantic import BaseModel
from typing import Optional

class OrganizationCreate(BaseModel):
    name: str
    slug: str

class UserCreate(BaseModel):
    organization_id: int
    full_name: str
    email: str
    password: str

class AssetCreate(BaseModel):
    organization_id: int
    name: str
    asset_type: str
    ip_address: Optional[str] = None
    domain: Optional[str] = None
    criticality: str = "medium"
    risk_level: str = "medium"

class FindingCreate(BaseModel):
    organization_id: int
    asset_id: Optional[int] = None
    title: str
    severity: str = "medium"
    category: Optional[str] = None
    description: str
    evidence: Optional[str] = None
    business_impact: Optional[str] = None
    recommendation: Optional[str] = None

class AttackPathCreate(BaseModel):
    organization_id: int
    name: str
    risk_level: str = "high"
    path_summary: str
    business_impact: Optional[str] = None
    lix_analysis: Optional[str] = None

class ThreatMemoryCreate(BaseModel):
    organization_id: int
    memory_type: str
    title: str
    summary: str
    severity: str = "medium"
    trend: str = "stable"

class ReportCreate(BaseModel):
    organization_id: int
    created_by: Optional[int] = None
    title: str
    report_type: str = "executive"
    language: str = "en"
    content: str

class LixRequest(BaseModel):
    organization_id: Optional[int] = None
    user_id: Optional[int] = None
    question: str
    context: Optional[str] = None
