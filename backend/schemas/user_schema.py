from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class User_Schema(BaseModel):
    """
    User should be created with below schema
    """
    email: EmailStr
    password: str = Field(..., min_length=4)


class Show_User(BaseModel):
    """
    The response should be shown with this schema
    """
    id: int
    email: EmailStr
    is_active: bool

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True

class User_Login_Schema(BaseModel):
    """
    User should be created with below schema
    """
    email: EmailStr
    password: str = Field(..., min_length=4)