from datetime import datetime

from ...db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Blogs(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    #author_id = Column(Integer, ForeignKey("user.id"))
    author_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"))
    author = relationship("Users", back_populates="blog")
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)
