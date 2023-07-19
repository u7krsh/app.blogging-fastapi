from backend.db.models.user import Users
from sqlalchemy.orm import Session


def get_user(email: str, db: Session):
    user = db.query(Users).filter(Users.email == email).first()
    return user
