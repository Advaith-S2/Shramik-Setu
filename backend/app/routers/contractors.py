"""
routers/contractors.py — M-03: Contractor Profile
Stub router — implement in Day 3.
PRD endpoints: GET /contractors/me, PUT /contractors/me,
               GET /contractors/me/dashboard
"""
from fastapi import APIRouter

router = APIRouter(prefix="/contractors", tags=["Contractors"])


@router.get("/me", summary="Get own contractor profile")
async def get_my_profile():
    # TODO (M-03 Day 3)
    return {"status": "stub", "message": "Not implemented — M-03 Day 3"}


@router.put("/me", summary="Update own contractor profile")
async def update_my_profile():
    # TODO (M-03 Day 3): validate, update contractors row, write audit log
    return {"status": "stub", "message": "Not implemented — M-03 Day 3"}


@router.get("/me/dashboard", summary="Get contractor dashboard overview data")
async def get_dashboard():
    # TODO (M-03 Day 3): aggregate projects, workers, attendance, wage summaries
    return {"status": "stub", "message": "Not implemented — M-03 Day 3"}
