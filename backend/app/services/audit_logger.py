"""
services/audit_logger.py — M-12: Cross-cutting Audit Trail
Every state-changing endpoint MUST call write_audit_log().
Stub — implement fully in Day 10 but the signature is frozen now.
"""
from typing import Any
import uuid


async def write_audit_log(
    *,
    user_id: str | None,
    action: str,
    entity_type: str,
    entity_id: str | uuid.UUID | None = None,
    details: dict[str, Any] | None = None,
    ip_address: str | None = None,
    db_client=None,  # Supabase client — injected in real impl
) -> None:
    """
    Insert one row into audit_logs.

    Args:
        user_id:     UUID of the acting user (None for system actions).
        action:      Dot-notation string, e.g. 'attendance.mark', 'payment.record'.
        entity_type: Table name of the affected entity, e.g. 'attendance'.
        entity_id:   UUID of the affected row.
        details:     Arbitrary JSONB context — include before/after values for mutations.
        ip_address:  Request IP from FastAPI Request object.
        db_client:   Supabase client (injected via dependency).

    IMPORTANT: This function must never raise — wrap in try/except in final impl
               so a logging failure never aborts the user-facing transaction.
    """
    # TODO (M-12 Day 10): insert into audit_logs via Supabase client
    #   Supabase RLS: INSERT allowed for service_role only; SELECT for inspector/admin.
    pass
