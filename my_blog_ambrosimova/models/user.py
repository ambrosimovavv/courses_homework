from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..db.session import Base

class User(Base):
    """

    username\
    email\
    password_hash\
    created_at\
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    comments = relationship("Comment", back_populates="users")
    posts = relationship("Post", back_populates="users")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
