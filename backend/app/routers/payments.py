"""
routers/payments.py — M-07: Payment Ledger
Stub router — implement in Day 7.
PRD endpoints: POST /payments, GET /payments/me, GET /payments/project/{id},
               GET /payments/{id}, GET /payments/{id}/receipt
IMPORTANT: No payment gateway. Insert-only ledger of declared payments.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/payments", tags=["Payments"])


@router.post("", summary="Record a payment declaration")
async def record_payment():
    # TODO (M-07 Day 7): insert payment_ledger row, update wage_records.actual_paid,
    # recalculate wage status, write audit log. NO UPI/Razorpay/Stripe.
    return {"status": "stub", "message": "Not implemented — M-07 Day 7"}


@router.get("/me", summary="Get worker's own payment history")
async def get_my_payments():
    # TODO (M-07 Day 7)
    return {"status": "stub", "message": "Not implemented — M-07 Day 7"}


@router.get("/project/{project_id}", summary="Get payments for a project")
async def get_project_payments(project_id: str):
    # TODO (M-07 Day 7): contractor/inspector view
    return {"status": "stub", "message": "Not implemented — M-07 Day 7"}


@router.get("/{payment_id}", summary="Get payment detail")
async def get_payment(payment_id: str):
    # TODO (M-07 Day 7)
    return {"status": "stub", "message": "Not implemented — M-07 Day 7"}


@router.get("/{payment_id}/receipt", summary="View payment receipt")
async def get_receipt(payment_id: str):
    # TODO (M-07 Day 7): return formatted receipt data for worker/contractor
    return {"status": "stub", "message": "Not implemented — M-07 Day 7"}
