# LN1 Deploy Ready Guide

This package prepares LN1 to run as a real web platform.

## Option 1: Run Locally with Docker

Requirements:
- Docker Desktop installed
- 4GB+ RAM recommended

Steps:

```bash
cp .env.production.example .env
docker compose -f docker-compose.prod.yml up --build
```

Open:

```text
Frontend: http://localhost:3000
Backend API: http://localhost:8000
Backend Docs: http://localhost:8000/docs
Health Check: http://localhost:8000/health
```

## Option 2: Run Backend Manually

```bash
cd backend
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Then:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Option 3: Run Frontend Manually

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

## Production Hosting Recommendation

For first public launch:

- Frontend: Vercel
- Backend: Render / Railway / VPS
- Database: Supabase PostgreSQL / Neon PostgreSQL
- Domain: lilexs.io

## Important

Before public launch:
- Replace JWT_SECRET
- Replace database password
- Configure HTTPS
- Configure proper CORS origins
- Connect Claude API to Lix
- Add real authentication
- Add payment provider only after validation
