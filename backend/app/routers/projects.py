"""
routers/projects.py — M-03: Projects (full)
Stub router — implement in Day 4.
PRD endpoints: POST /projects, GET /projects, GET /projects/{id},
               PUT /projects/{id}, DELETE /projects/{id},
               GET /projects/{id}/location
"""
from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("", summary="Create a new project")
async def create_project():
    # TODO (M-03 Day 4)
    return {"status": "stub", "message": "Not implemented — M-03 Day 4"}


@router.get("", summary="List contractor's own projects")
async def list_projects():
    # TODO (M-03 Day 4)
    return {"status": "stub", "message": "Not implemented — M-03 Day 4"}


@router.get("/{project_id}", summary="Get project detail")
async def get_project(project_id: str):
    # TODO (M-03 Day 4)
    return {"status": "stub", "message": "Not implemented — M-03 Day 4"}


@router.put("/{project_id}", summary="Update a project")
async def update_project(project_id: str):
    # TODO (M-03 Day 4): validate, update, write audit log
    return {"status": "stub", "message": "Not implemented — M-03 Day 4"}


@router.delete("/{project_id}", summary="Soft-delete a project")
async def delete_project(project_id: str):
    # TODO (M-03 Day 4): set status='cancelled', write audit log
    return {"status": "stub", "message": "Not implemented — M-03 Day 4"}


@router.get("/{project_id}/location", summary="Get GPS location + radius for project")
async def get_project_location(project_id: str):
    # TODO (M-03 Day 4): return project_locations row
    return {"status": "stub", "message": "Not implemented — M-03 Day 4"}
