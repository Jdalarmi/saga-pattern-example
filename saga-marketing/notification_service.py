from .schemas.schemas import PostResponse

def send_notification(post_id: str) -> PostResponse:
    return PostResponse(post_id=post_id, status="notification_sent")

def retract_notification(post_id: str) -> PostResponse:
    return PostResponse(post_id=post_id, status="notification_retracted")
