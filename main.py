from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/hello")
def index():
    return {"message" : "Hello World"}

# @app.get('/blog/all')
# def get_blog():
#     return {'message' : f'all blogs provided'}

@app.get('/blog/all')
def get_all_blog(page=1, page_size: Optional[int] = None):
    return {'message' : f'All {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message' : f'Blog id {id}, comment id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message' : f'Blog type {type}'}

@app.get('/blog/{id}')
def get_blog(id : int):
    return {'message' : f'Blog with id {id}'}