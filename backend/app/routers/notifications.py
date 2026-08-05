"""
routers/notifications.py — M-11: In-App Notifications
Stub router — implement in Day 11.
PRD endpoints: GET /notifications, GET /notifications/unread-count,
               PUT /notifications/{id}/read, PUT /notifications/read-all
No SMS/email/push in MVP.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.get("", summary="List notifications for current user")
async def list_notifications():
    # TODO (M-11 Day 11): paginated list, newest first
    return {"status": "stub", "message": "Not implemented — M-11 Day 11"}


@router.get("/unread-count", summary="Get count of unread notifications")
async def get_unread_count():
    # TODO (M-11 Day 11): count WHERE is_read = FALSE AND user_id = current
    return {"status": "stub", "message": "Not implemented — M-11 Day 11"}


@router.put("/{notification_id}/read", summary="Mark a notification as read")
async def mark_read(notification_id: str):
    # TODO (M-11 Day 11): set is_read = TRUE
    return {"status": "stub", "message": "Not implemented — M-11 Day 11"}


@router.put("/read-all", summary="Mark all notifications as read")
async def mark_all_read():
    # TODO (M-11 Day 11): bulk update WHERE user_id = current AND is_read = FALSE
    return {"status": "stub", "message": "Not implemented — M-11 Day 11"}
