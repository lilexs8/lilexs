from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base, engine
from app.models import core
from app.api.routes import mission_control, assets, findings, attack_paths, threat_memory, reports, lix

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LN1 Production V1 API",
    description="AI-Powered Security Intelligence Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mission_control.router)
app.include_router(assets.router)
app.include_router(findings.router)
app.include_router(attack_paths.router)
app.include_router(threat_memory.router)
app.include_router(reports.router)
app.include_router(lix.router)




@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "product": "LN1",
        "assistant": "Lix"
    }
