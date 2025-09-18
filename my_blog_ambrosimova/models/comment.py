from datetime import datetime
from email.policy import default

from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from ..db.session import Base

class Comment(Base):
    """

    message \
    date_create \
    post_id \
    user_id \
    """
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=False)
    date_create = Column(DateTime, default=datetime.now())
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    posts = relationship('Post', back_populates="comments")
    users = relationship('User', back_populates='comments')

