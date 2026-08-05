"""
routers/workers.py — M-02: Worker Profile
Stub router — implement in Day 3.
PRD endpoints: GET /workers/me, PUT /workers/me,
               POST /workers/me/photo, PUT /workers/me/preferences
"""
from fastapi import APIRouter

router = APIRouter(prefix="/workers", tags=["Workers"])


@router.get("/me", summary="Get own worker profile")
async def get_my_profile():
    # TODO (M-02 Day 3)
    return {"status": "stub", "message": "Not implemented — M-02 Day 3"}


@router.put("/me", summary="Update own worker profile")
async def update_my_profile():
    # TODO (M-02 Day 3): validate with Pydantic, update workers row, write audit log
    return {"status": "stub", "message": "Not implemented — M-02 Day 3"}


@router.post("/me/photo", summary="Upload worker profile photo")
async def upload_photo():
    # TODO (M-02 Day 3): upload to Supabase Storage, update photo_url
    return {"status": "stub", "message": "Not implemented — M-02 Day 3"}


@router.put("/me/preferences", summary="Update language preferences")
async def update_preferences():
    # TODO (M-02 Day 3): upsert user_preferences row
    return {"status": "stub", "message": "Not implemented — M-02 Day 3"}
