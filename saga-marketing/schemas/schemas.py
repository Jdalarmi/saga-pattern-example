from pydantic import BaseModel

class Post(BaseModel):
    post_id: str
    title: str
    content: str

class PostResponse(BaseModel):
    post_id: str
    status: str
    detail: str = None