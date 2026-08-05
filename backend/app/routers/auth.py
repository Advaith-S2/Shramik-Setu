"""
routers/auth.py — M-01: Authentication & Role Management
Stub router — implement in Day 2.
PRD endpoints: POST /auth/register, POST /auth/login, POST /auth/logout,
               POST /auth/password-reset/request, GET /auth/me
"""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", summary="Register a new user")
async def register():
    # TODO (M-01 Day 2): validate input, create Supabase Auth user, insert users row
    return {"status": "stub", "message": "Not implemented — M-01 Day 2"}


@router.post("/login", summary="Login and receive JWT")
async def login():
    # TODO (M-01 Day 2): Supabase signInWithPassword, return JWT
    return {"status": "stub", "message": "Not implemented — M-01 Day 2"}


@router.post("/logout", summary="Invalidate session")
async def logout():
    # TODO (M-01 Day 2): Supabase signOut
    return {"status": "stub", "message": "Not implemented — M-01 Day 2"}


@router.post("/password-reset/request", summary="Request password reset email")
async def password_reset_request():
    # TODO (M-01 Day 2): Supabase resetPasswordForEmail
    return {"status": "stub", "message": "Not implemented — M-01 Day 2"}


@router.get("/me", summary="Get current authenticated user")
async def get_me():
    # TODO (M-01 Day 2): decode JWT, return user profile
    return {"status": "stub", "message": "Not implemented — M-01 Day 2"}
