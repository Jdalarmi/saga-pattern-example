from .schemas.schemas import PostResponse

def publish_post(post_id: str) -> PostResponse:
    if post_id == "123":
        raise Exception("Falha ao publicar no site")
    return PostResponse(post_id=post_id, status="published")

def retract_post(post_id: str) -> PostResponse:
    return PostResponse(post_id=post_id, status="retracted")
