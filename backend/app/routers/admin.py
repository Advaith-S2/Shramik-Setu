"""
routers/admin.py — Admin utilities
Stub router — implement when needed.
PRD endpoints: PUT /admin/users/{id}/role, PUT /admin/minimum-wages
Also includes: GET /audit-logs, GET /audit-logs/entity/{type}/{id}
"""
from fastapi import APIRouter

router = APIRouter(tags=["Admin & Audit"])


@router.put("/admin/users/{user_id}/role", summary="Admin: change a user's role")
async def change_user_role(user_id: str):
    # TODO: admin-only; update users.role, write audit log
    return {"status": "stub", "message": "Not implemented — Admin"}


@router.put("/admin/minimum-wages", summary="Admin: update minimum wage reference data")
async def update_minimum_wages():
    # TODO: admin-only; upsert minimum_wages rows
    return {"status": "stub", "message": "Not implemented — Admin"}


@router.get("/audit-logs", summary="Inspector/Admin: query audit log")
async def list_audit_logs():
    # TODO (M-12 Day 10): filterable by entity_type, entity_id, user_id, date range
    return {"status": "stub", "message": "Not implemented — M-12 Day 10"}


@router.get("/audit-logs/entity/{entity_type}/{entity_id}", summary="Audit log for a specific entity")
async def get_entity_audit_log(entity_type: str, entity_id: str):
    # TODO (M-12 Day 10)
    return {"status": "stub", "message": "Not implemented — M-12 Day 10"}
