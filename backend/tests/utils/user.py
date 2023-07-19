from db.repository.user import create_new_user
from schemas.user_schema import User_Schema
from sqlalchemy.orm.session import Session


def create_random_user(db: Session):
    user = User_Schema(email="ping@fastapitutorial.com", password="Hello!")
    user = create_new_user(user=user, db=db)
    return user
