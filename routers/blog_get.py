from fastapi import APIRouter, Response, status, Depends
from enum import Enum
from typing import Optional
from routers import required_functionality

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


# @router.get('/blog/all')
# def get_all_blogs():
#   return {'message': 'All blogs provided'}

@router.get(
    '/all',
    summary='Retrieve all blogs',
    description='This api calls simulates fetching all blogs',
    response_description='The list of available blogs',
    )
def get_blogs(page = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
  return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """simulates retrieving a comment of a blog

    Args:
    - **id** (int): mandatory path parameter
    - **comment_id** (int): mandatory path parameter
    - **valid** (bool, optional):optional query parameter. Defaults to True.
    - **username** (Optional[str], optional): ptional query parameter Defaults to None.

    Returns:
        str: info regarding the comment
    """
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{type}')
def get_blog_type(type: BlogType, req_parameter: dict = Depends(required_functionality)):
  return {'message': f'Blog type {type}'}

@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response, req_parameter: dict = Depends(required_functionality)):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog {id} not found'}
  else : 
    response.status_code = status.HTTP_200_OK
    return {'message': f'Blog with id {id}'}
