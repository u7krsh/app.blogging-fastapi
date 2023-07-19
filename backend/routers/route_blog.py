from backend.db.repository.blog import create_new_blog
from backend.db.repository.blog import delete_blog_from_db
from backend.db.repository.blog import retrieve_all_blogs
from backend.db.repository.blog import retrieve_blog
from backend.db.repository.blog import update_blog_in_db
from backend.db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from backend.schemas.blog_schema import Blog_Schema
from backend.schemas.blog_schema import Show_Blog_Schema
from backend.schemas.blog_schema import Update_Blog_Schema
from sqlalchemy.orm import Session
from backend.db.models.user import Users #new
from backend.routers.route_login import get_current_user

router = APIRouter()


@router.post(
    "/", response_model=Show_Blog_Schema, status_code=status.HTTP_201_CREATED
)  # modified
def create_blog(blog: Blog_Schema, db: Session = Depends(get_db), current_user: Users=Depends(get_current_user)):
    blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return blog


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= Show_Blog_Schema)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog_details = retrieve_blog(id=id, db=db)
    if not blog_details:
        raise HTTPException(
            detail=f"Blog with id {id} not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return blog_details


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_blogs(db: Session = Depends(get_db), current_user: Users=Depends(get_current_user)):
    blog_details = retrieve_all_blogs(db=db, user_id=current_user.id)
    if not blog_details:
        raise HTTPException(
            detail=f"Blog with id {id} not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return blog_details


@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, blog_data: Update_Blog_Schema, db: Session = Depends(get_db),  current_user: Users=Depends(get_current_user)):
    blog_details = update_blog_in_db(id=id, blog=blog_data, db=db, author_id=current_user.id)
    if not blog_details:
        raise HTTPException(
            detail=f"Blog with id {id} not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return blog_details


@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), current_user: Users=Depends(get_current_user)):
    blog_details = delete_blog_from_db(id=id, dbh=db, author_id=current_user.id)
    if blog_details.get("error"):
        raise HTTPException(
            detail=blog_details.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": f"Successfully deleted blog with id {id}"}