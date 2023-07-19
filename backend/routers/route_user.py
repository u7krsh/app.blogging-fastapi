from backend.db.repository.user import create_new_user, get_users
from backend.db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status, HTTPException
from backend.schemas.user_schema import Show_User
from backend.schemas.user_schema import User_Schema
from sqlalchemy.orm import Session


router = APIRouter()


@router.post(
    "/", response_model=Show_User, status_code=status.HTTP_201_CREATED
)  # modified
def create_user(user: User_Schema, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user

@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=Show_User
)
def show_users(db: Session = Depends(get_db)):
    user = get_users(db=db)
    print(user)
    return user 

@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=Show_User
)
def show_users(id: int, db: Session = Depends(get_db)):
    user = get_users(user_id=id, db=db)
    if not user:
        raise HTTPException(
            detail=f"User with id {id} not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return user 