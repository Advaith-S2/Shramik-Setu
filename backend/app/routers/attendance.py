"""
routers/attendance.py — M-05: Attendance + GPS
Stub router — implement in Day 5.
PRD endpoints: POST /attendance/pin/generate, POST /attendance/check-location,
               POST /attendance/mark, GET /attendance/me,
               GET /attendance/project/{id}, POST /attendance/{id}/override
"""
from fastapi import APIRouter

router = APIRouter(prefix="/attendance", tags=["Attendance"])


@router.post("/pin/generate", summary="Generate daily attendance PIN")
async def generate_pin():
    # TODO (M-05 Day 5): generate PIN, SHA-256 hash, store in attendance row
    return {"status": "stub", "message": "Not implemented — M-05 Day 5"}


@router.post("/check-location", summary="Validate worker GPS against project geofence")
async def check_location():
    # TODO (M-05 Day 5): call haversine service, return within_radius + distance_m
    return {"status": "stub", "message": "Not implemented — M-05 Day 5"}


@router.post("/mark", summary="Mark attendance (PIN + GPS)")
async def mark_attendance():
    # TODO (M-05 Day 5): validate PIN hash, validate GPS, insert attendance + verification rows
    # Write audit log. 5 attempts/day limit per PRD §11.5.
    return {"status": "stub", "message": "Not implemented — M-05 Day 5"}


@router.get("/me", summary="Get worker's own attendance history")
async def get_my_attendance():
    # TODO (M-05 Day 5): filter attendance by current worker_id
    return {"status": "stub", "message": "Not implemented — M-05 Day 5"}


@router.get("/project/{project_id}", summary="Get attendance records for a project")
async def get_project_attendance(project_id: str):
    # TODO (M-05 Day 5): contractor/supervisor view
    return {"status": "stub", "message": "Not implemented — M-05 Day 5"}


@router.post("/{attendance_id}/override", summary="Supervisor GPS override")
async def override_attendance(attendance_id: str):
    # TODO (M-05 Day 5): set method='override', store override_reason, write audit log
    return {"status": "stub", "message": "Not implemented — M-05 Day 5"}
