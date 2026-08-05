"""
routers/disputes.py — M-09: Disputes
Stub router — implement in Day 9.
PRD endpoints: POST /disputes, GET /disputes/me, GET /disputes,
               POST /disputes/{id}/respond, PUT /disputes/{id}/resolve
Workflow (frozen): Raise → Contractor responds → Inspector resolves (AGENTS.md §1)
"""
from fastapi import APIRouter

router = APIRouter(prefix="/disputes", tags=["Disputes"])


@router.post("", summary="Worker raises a dispute")
async def raise_dispute():
    # TODO (M-09 Day 9): insert disputes row (status='open'), notify contractor, write audit log
    return {"status": "stub", "message": "Not implemented — M-09 Day 9"}


@router.get("/me", summary="Worker's own disputes")
async def get_my_disputes():
    # TODO (M-09 Day 9)
    return {"status": "stub", "message": "Not implemented — M-09 Day 9"}


@router.get("", summary="Inspector: list all disputes (filterable)")
async def list_all_disputes():
    # TODO (M-09 Day 9): inspector-only; filter by status, priority, district
    return {"status": "stub", "message": "Not implemented — M-09 Day 9"}


@router.post("/{dispute_id}/respond", summary="Contractor responds to dispute")
async def respond_to_dispute(dispute_id: str):
    # TODO (M-09 Day 9): set contractor_response, status='contractor_responded', write audit log
    return {"status": "stub", "message": "Not implemented — M-09 Day 9"}


@router.put("/{dispute_id}/resolve", summary="Inspector resolves a dispute")
async def resolve_dispute(dispute_id: str):
    # TODO (M-09 Day 9): set resolution, resolved_by, status, write audit log
    return {"status": "stub", "message": "Not implemented — M-09 Day 9"}
