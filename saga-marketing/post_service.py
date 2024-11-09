from .schemas.schemas import Post, PostResponse


def create_post(post: Post) -> PostResponse:
    return PostResponse(post_id=post.post_id, status="created")

def delete_post(post_id: str) -> PostResponse:
    return PostResponse(post_id=post_id, status="deleted")
