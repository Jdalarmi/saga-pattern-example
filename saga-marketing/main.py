from fastapi import FastAPI
from .schemas.schemas import Post, PostResponse
from .saga_orchestrator import process_post_saga


app = FastAPI()

@app.post('/posts', response_model=PostResponse)
async def create_marketing_post(post: Post):
    return process_post_saga(post)
