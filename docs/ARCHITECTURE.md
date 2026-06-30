# LN1 Production V1 Architecture

```text
User
  ↓
Next.js Frontend
  ↓
FastAPI Backend
  ↓
PostgreSQL Database

FastAPI also connects to:
- Lix service
- Reports service
- Threat Memory service
- Attack Path Intelligence
```

## Deployment Modes

- Local development
- SaaS deployment
- Future on-premise deployment
