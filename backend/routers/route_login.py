from datetime import timedelta

from backend.core.config import settings  #new
from backend.core.hashing import Hasher
from backend.core.security import create_access_token
from backend.db.repository.login import get_user
from backend.db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer #new
from jose import JWTError, jwt   #new
from backend.schemas.token_schema import Token_Schema
from backend.schemas.user_schema import User_Login_Schema
from sqlalchemy.orm import Session


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authenticate_user(email: str, password: str, db: Session) -> bool:
    user = get_user(email=email, db=db)
    if user and Hasher.verify_password(password, user.password):
        return user
    return False


@router.post("/", response_model=Token_Schema)
def login_for_access_token(
    formdata: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # authenticate user in db
    # return unauthorized if no user found
    # Post authentication, return acess token
    user = authenticate_user(formdata.username, formdata.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Invalid Credentials",
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError as exp:
        print(exp)
        raise credentials_exception

def get_current_user(token: str = Depends(oauth2_scheme), db: Session= Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    username = verify_access_token(token, credentials_exception)
    user = get_user(email=username, db=db)
    if user is None:
        raise credentials_exception
    return user