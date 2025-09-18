from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from ..db.session import Base

class Post(Base):
    """

    title
    message
    date_create
    user_id
    tag_id
    """
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    date_create = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))

    users = relationship('User', back_populates='posts')
    tags = relationship('Tag', back_populates='posts')
    comments = relationship('Comment', back_populates='posts')

