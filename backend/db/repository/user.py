from backend.core.hashing import Hasher  # For passwd hashing
from backend.db.models.user import Users  # Import model
from backend.schemas.user_schema import User_Schema, Show_User  # Get user schema
from sqlalchemy.orm import Session


def create_new_user(user: User_Schema, db: Session) -> Users:
    user = Users(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session, user_id = None) -> Users:
    if user_id is None:
        user = db.query(Users).all()
    else:
        user = db.query(Users).filter(Users.id==user_id).first()
    return user