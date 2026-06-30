from app.db.session import SessionLocal, Base, engine
from app.models.core import Organization, Asset, Finding, AttackPath, ThreatMemory, Report

Base.metadata.create_all(bind=engine)
db = SessionLocal()

org = Organization(name="Demo Organization", slug="demo-org", plan="nexus")
db.add(org)
db.commit()
db.refresh(org)

web = Asset(organization_id=org.id, name="Web Server", asset_type="server", ip_address="10.0.0.10", criticality="high", risk_level="high")
identity = Asset(organization_id=org.id, name="Identity Service", asset_type="identity", ip_address="10.0.0.20", criticality="critical", risk_level="critical")
db.add_all([web, identity])
db.commit()

finding = Finding(
    organization_id=org.id,
    asset_id=identity.id,
    title="Exposed Identity Service",
    severity="critical",
    category="identity",
    description="Identity service is reachable from an untrusted network segment.",
    business_impact="Potential unauthorized access to sensitive systems.",
    recommendation="Restrict access, enforce MFA, and segment identity systems."
)
db.add(finding)

path = AttackPath(
    organization_id=org.id,
    name="External Web to Sensitive Data",
    risk_level="critical",
    path_summary="Internet -> Web Server -> Identity Service -> Database",
    business_impact="Potential exposure of sensitive organizational data.",
    lix_analysis="Lix recommends prioritizing identity segmentation and MFA enforcement."
)
db.add(path)

memory = ThreatMemory(
    organization_id=org.id,
    memory_type="recurring-risk",
    title="Repeated Identity Exposure",
    summary="Identity-related risks appeared repeatedly in recent assessments.",
    severity="high",
    trend="declining"
)
db.add(memory)

report = Report(
    organization_id=org.id,
    title="Executive Risk Summary",
    report_type="executive",
    content="LN1 detected critical identity exposure connected to sensitive data paths."
)
db.add(report)

db.commit()
db.close()
print("LN1 Production V1 demo data created.")
