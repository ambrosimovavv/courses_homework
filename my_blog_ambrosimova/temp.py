from requests import session

from db.session import Session
from models.post import Post
from models.comment import Comment
from models.user import User
from models.tag import Tag


session = Session()
