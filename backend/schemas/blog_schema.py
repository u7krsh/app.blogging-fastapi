from datetime import date
from typing import Optional, Any

from pydantic import BaseModel


class Blog_Schema(BaseModel):
    title: str
    content: Optional[str] = None


class Update_Blog_Schema(Blog_Schema):
    pass


class Show_Blog_Schema(BaseModel):
    title: str
    content: Optional[str]
    created_at: date
    author: Any

    class Config:
        orm_mode = True
