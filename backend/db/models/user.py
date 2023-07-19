from backend.db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Users(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    blog = relationship("Blogs", back_populates="author")
