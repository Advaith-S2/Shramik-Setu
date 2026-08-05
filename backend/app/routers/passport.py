"""
routers/passport.py — M-08: Employment Passport PDF
Stub router — implement in Day 8.
PRD endpoints: GET /passport/me, GET /passport/{worker_id},
               POST /passport/me/export
"""
from fastapi import APIRouter

router = APIRouter(prefix="/passport", tags=["Employment Passport"])


@router.get("/me", summary="Get worker's own employment passport data")
async def get_my_passport():
    # TODO (M-08 Day 8): aggregate contracts, attendance, wage_records, payment_ledger
    return {"status": "stub", "message": "Not implemented — M-08 Day 8"}


@router.get("/{worker_id}", summary="Inspector views a worker's passport")
async def get_worker_passport(worker_id: str):
    # TODO (M-08 Day 8): inspector-only
    return {"status": "stub", "message": "Not implemented — M-08 Day 8"}


@router.post("/me/export", summary="Generate and download Employment Passport PDF")
async def export_passport_pdf():
    # TODO (M-08 Day 8): call pdf_generator service (ReportLab), stream PDF response
    # Rate limit: 1 req/30s per PRD §11.5. Include Devanagari font support.
    return {"status": "stub", "message": "Not implemented — M-08 Day 8"}
