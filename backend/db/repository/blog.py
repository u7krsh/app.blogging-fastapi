from typing import Dict

from ...db.models.blog import Blogs  # Import model
from backend.schemas.blog_schema import Blog_Schema
from backend.schemas.blog_schema import Update_Blog_Schema
from sqlalchemy.orm import Session


def create_new_blog(blog: Blog_Schema, db: Session, author_id: int) -> Blogs:
    blog = Blogs(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(id: int, db: Session) -> Blogs:
    blog = db.query(Blogs).filter(Blogs.id == id).first()
    return blog


def retrieve_all_blogs(db: Session, user_id: int) -> Blogs:
    blogs = db.query(Blogs).filter(Blogs.author_id==user_id).all()
    return blogs


def update_blog_in_db(id: int, blog: Update_Blog_Schema, author_id: int, db: Session):
    blog_in_db = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog_in_db:
        return {"error":f"Blogs with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:                   #new
        return {"error":f"Only the author can modify the blog"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.refresh(blog)
    db.commit()
    return blog_in_db


def delete_blog_from_db(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blogs).filter(Blogs.id == id)
    if not blog_in_db.first():
        return {"error": f"Could not find blog with id {id}"}
    if not blog_in_db.first().author_id ==author_id:             #new
        return {"error":f"Only the author can delete a blog"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"deleted blog with id {id}"}
