FROM node:20-alpine AS frontend-build
WORKDIR /frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
ENV NEXT_TELEMETRY_DISABLED=1
RUN npm run build 2>&1

FROM python:3.11-slim
WORKDIR /app
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/app ./app
COPY backend/seed.py ./seed.py
COPY --from=frontend-build /frontend/out ./static
ENV PORT=8000
EXPOSE 8000
CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
