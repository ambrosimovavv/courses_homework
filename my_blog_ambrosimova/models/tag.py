from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from ..db.session import Base
class Tag(Base):
    """

    message
    """
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    message = Column(Text, nullable=False)

    posts = relationship('Post', back_populates="tags")

