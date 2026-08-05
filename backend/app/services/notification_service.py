"""
services/notification_service.py — M-11: In-App Notifications
In-app only. No SMS/email/push in MVP (AGENTS.md §1).
Stub — implement in Day 11.
"""


async def send_notification(
    *,
    user_id: str,
    title: str,
    body: str,
    notification_type: str,
    link: str | None = None,
    db_client=None,
) -> None:
    """
    Insert a notification row for a user.

    Args:
        user_id:           Target user's UUID.
        title:             Short notification title (translated key or final string).
        body:              Full notification body.
        notification_type: e.g. 'contract_accepted', 'payment_received',
                           'dispute_raised', 'dispute_resolved', 'attendance_override'.
        link:              Frontend route to navigate on click, e.g. '/en/worker/contracts'.
        db_client:         Supabase client (injected via dependency).

    Note: Call this from routers after state-changing operations.
          Never send SMS/email/push — in-app queue only.
    """
    # TODO (M-11 Day 11): insert into notifications table
    raise NotImplementedError("notification_service — implement in Day 11 (M-11)")
