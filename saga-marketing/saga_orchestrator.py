from .schemas.schemas import Post, PostResponse
from .post_service import create_post, delete_post
from .notification_service import send_notification, retract_notification
from .website_service import publish_post, retract_post
import time


MAX_RETRIES = 3
RETRY_INTERVAL = 2

def process_post_saga(post: Post) -> PostResponse:
    try:
        create_post(post)

        send_notification(post.post_id)

        retry_count = 0
        while retry_count < MAX_RETRIES:
            try:
                publish_post(post.post_id)
                break
            except Exception as e:
                retry_count += 1
                time.sleep(RETRY_INTERVAL)
                if retry_count == MAX_RETRIES:
                    raise e
        return PostResponse(post_id=post.post_id, status="completed")
    except Exception as e:
        retract_notification(post.post_id)
        delete_post(post.post_id)
        return PostResponse(post_id=post.post_id, status='failed', detail=str(e))