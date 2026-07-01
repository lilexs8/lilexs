from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from app.db.session import Base, engine
from app.models import core
from app.api.routes import mission_control, assets, findings, attack_paths, threat_memory, reports, lix

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LN1 API", docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api = APIRouter(prefix="/api")
api.include_router(mission_control.router)
api.include_router(assets.router)
api.include_router(findings.router)
api.include_router(attack_paths.router)
api.include_router(threat_memory.router)
api.include_router(reports.router)
api.include_router(lix.router)
app.include_router(api)

@app.get("/health")
def health():
    return {"status": "healthy"}

STATIC = "/app/static"

@app.get("/")
def root():
    return FileResponse(f"{STATIC}/index.html")

@app.get("/{full_path:path}")
def spa(full_path: str):
    file = f"{STATIC}/{full_path}"
    if os.path.isfile(file):
        return FileResponse(file)
    index = f"{STATIC}/{full_path}/index.html"
    if os.path.isfile(index):
        return FileResponse(index)
    return FileResponse(f"{STATIC}/index.html")
