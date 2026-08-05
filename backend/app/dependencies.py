"""
dependencies.py — ShramikSetu Backend
FastAPI dependency-injection helpers.
All stubs for Day 1; real implementations in M-01 (Auth, Day 2).
"""
from fastapi import Header, HTTPException, status
from app.config import get_settings


async def get_current_user(authorization: str = Header(default="")):
    """
    Stub dependency — returns a placeholder user dict.
    Day 2: validate Supabase JWT, extract user_id + role from claims.
    """
    # TODO (M-01 Day 2): verify JWT signature, decode claims
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Auth not yet implemented. Implement in M-01 (Day 2).",
    )


async def require_role(*allowed_roles: str):
    """
    Factory for role-gated dependencies.
    Usage: Depends(require_role('contractor', 'admin'))
    Day 2: real RBAC check after get_current_user is wired.
    """
    # TODO (M-01 Day 2): inject get_current_user, check role membership
    async def _checker(authorization: str = Header(default="")):
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="RBAC not yet implemented. Implement in M-01 (Day 2).",
        )
    return _checker
