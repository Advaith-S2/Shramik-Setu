"""
routers/contracts.py — M-04: QR Contracts
Stub router — implement in Day 4.
PRD endpoints: POST /projects/{id}/contracts/qr,
               GET /contracts/accept/{token}, POST /contracts/accept/{token},
               GET /contracts/me, GET /contracts/{id}
"""
from fastapi import APIRouter

router = APIRouter(tags=["Contracts / QR"])


@router.post("/projects/{project_id}/contracts/qr", summary="Generate QR contract for a project")
async def generate_qr(project_id: str):
    # TODO (M-04 Day 4): generate qr_token (UUID), call qr_generator service, store contract row
    return {"status": "stub", "message": "Not implemented — M-04 Day 4"}


@router.get("/contracts/accept/{token}", summary="Get contract details by QR token")
async def get_contract_by_token(token: str):
    # TODO (M-04 Day 4): lookup contract by qr_token, check expiry
    return {"status": "stub", "message": "Not implemented — M-04 Day 4"}


@router.post("/contracts/accept/{token}", summary="Worker accepts contract via QR token")
async def accept_contract(token: str):
    # TODO (M-04 Day 4): set status='accepted', accepted_at=now(), write audit log
    return {"status": "stub", "message": "Not implemented — M-04 Day 4"}


@router.get("/contracts/me", summary="List worker's own contracts")
async def list_my_contracts():
    # TODO (M-04 Day 4): filter contracts by current worker_id
    return {"status": "stub", "message": "Not implemented — M-04 Day 4"}


@router.get("/contracts/{contract_id}", summary="Get contract detail")
async def get_contract(contract_id: str):
    # TODO (M-04 Day 4)
    return {"status": "stub", "message": "Not implemented — M-04 Day 4"}
