"""
routers/wages.py — M-06: Wage Calculator
Stub router — implement in Day 6.
PRD endpoints: GET /wages/me, GET /wages/project/{id},
               GET /wages/summary/{project_id}
"""
from fastapi import APIRouter

router = APIRouter(prefix="/wages", tags=["Wages"])


@router.get("/me", summary="Get worker's own wage records")
async def get_my_wages():
    # TODO (M-06 Day 6): return wage_records for current worker
    return {"status": "stub", "message": "Not implemented — M-06 Day 6"}


@router.get("/project/{project_id}", summary="Get wage records for a project")
async def get_project_wages(project_id: str):
    # TODO (M-06 Day 6): contractor/inspector view; filter by project
    return {"status": "stub", "message": "Not implemented — M-06 Day 6"}


@router.get("/summary/{project_id}", summary="Get payroll summary for a project")
async def get_payroll_summary(project_id: str):
    # TODO (M-06 Day 6): aggregate expected vs actual paid across all workers
    return {"status": "stub", "message": "Not implemented — M-06 Day 6"}
