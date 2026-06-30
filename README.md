# LN1 Production V1

**Brand:** Lilexs  
**Product:** LN1  
**Assistant:** Lix  
**Tagline:** Hunt the risk before it hunts you.

LN1 Production V1 is the real project foundation for an AI-powered security intelligence platform.

## Modules Included

- FastAPI backend (Mission Control, Assets, Findings, Attack Paths, Threat Memory, Reports, Lix)
- Next.js frontend with live pages for every module + an interactive Lix chat UI
- PostgreSQL schema (SQLite by default for local dev)
- Docker Compose (dev + prod, now including the frontend service)
- Lix wired to the real Claude API (falls back to rule-based answers automatically if no key is set)
- Documentation and roadmap

## Important Safety Scope

LN1 is designed for authorized defensive security assessment, risk intelligence, reporting, and security posture management.

## Quick Start

### 1. Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
python seed.py            # optional: creates demo data
uvicorn app.main:app --reload
```

### 2. Frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local   # set NEXT_PUBLIC_API_URL if needed
npm run dev
```

Visit http://localhost:3000 for Mission Control, Assets, Findings, Attack Paths, Threat Memory, Reports, and Ask Lix.

### 3. Docker

```bash
docker compose up --build
```

This now starts Postgres, the backend, and the frontend together.

### 4. Enable real Lix (Claude API)

Set `CLAUDE_API_KEY` in `backend/.env` (or as an env var / Docker env) to your Anthropic API key.
Lix will automatically switch from rule-based answers to live Claude responses — no code changes needed.

## Recommended Next Steps

1. Connect PostgreSQL in production (already wired, just set `DATABASE_URL`).
2. Implement JWT auth (login endpoints + protected routes).
3. Add per-organization auth/session handling to the frontend (currently uses `organization_id=1` by default).
4. Add safe scanner import integrations.
5. Add report PDF export.


## Deploy Ready Update

This version includes:
- Production Docker Compose
- Frontend Dockerfile
- Backend health endpoint
- Vercel config
- Render config
- Deployment guide
- Production environment template

See `DEPLOYMENT_GUIDE.md`.
