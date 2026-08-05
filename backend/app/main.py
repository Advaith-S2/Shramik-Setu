"""
main.py — ShramikSetu FastAPI Application Entry Point
Run locally: uvicorn app.main:app --reload --port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routers import (
    auth,
    workers,
    contractors,
    projects,
    contracts,
    attendance,
    wages,
    payments,
    disputes,
    passport,
    inspector,
    notifications,
    admin,
)

settings = get_settings()

app = FastAPI(
    title="ShramikSetu API",
    description=(
        "Digital Employment, Wage Verification & Benefit Platform "
        "for India's Unorganised Workforce. API v1."
    ),
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────────
API_PREFIX = "/api/v1"

app.include_router(auth.router,          prefix=API_PREFIX)
app.include_router(workers.router,       prefix=API_PREFIX)
app.include_router(contractors.router,   prefix=API_PREFIX)
app.include_router(projects.router,      prefix=API_PREFIX)
app.include_router(contracts.router,     prefix=API_PREFIX)   # Mixed prefixes — see contracts.py
app.include_router(attendance.router,    prefix=API_PREFIX)
app.include_router(wages.router,         prefix=API_PREFIX)
app.include_router(payments.router,      prefix=API_PREFIX)
app.include_router(disputes.router,      prefix=API_PREFIX)
app.include_router(passport.router,      prefix=API_PREFIX)
app.include_router(inspector.router,     prefix=API_PREFIX)
app.include_router(notifications.router, prefix=API_PREFIX)
app.include_router(admin.router,         prefix=API_PREFIX)


# ── Health check ──────────────────────────────────────────────────────────────
@app.get("/health", tags=["Health"], summary="Liveness check")
async def health():
    """Returns 200 OK if the server is running. Used by Render health checks."""
    return {"status": "ok", "version": app.version}


# ── Root redirect ─────────────────────────────────────────────────────────────
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "ShramikSetu API — see /docs for Swagger UI"}
