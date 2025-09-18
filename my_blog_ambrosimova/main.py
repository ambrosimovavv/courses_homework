import datetime

from .db.session import Session
from .models.comment import Comment
from .models.post import Post
from .models.user import User
from .models.tag import Tag


if __name__ == '__main__':

    session = Session()
    new_user1 = User(username="Andrew Popov",
                     email="ppand@mail.ru",
                     password_hash="jeenko",
                     created_at=datetime.datetime.now())
    session.add(new_user1)
    new_user2 = User(username="Alex Ivanov",
                     email="iv_al@mail.ru",
                     password_hash="jeenko",
                     created_at=datetime.datetime.now())
    session.add(new_user2)
    new_user3 = User(username="Anna Sidorova",
                     email="sidorova@mail.ru",
                     password_hash="jeenko",
                     created_at=datetime.datetime.now())
    session.add(new_user3)
    session.commit()

    new_tag1 = Tag(message="первый")
    session.add(new_tag1)
    new_tag2 = Tag(message="второй")
    session.add(new_tag2)

    session.commit()

    new_post1 = Post(title="Первый пост",
                    message="это мой первый пост. Привет!",
                    date_create=datetime.datetime.now(),
                    user_id=new_user1.id,
                    tag_id=new_tag1.id)
    session.add(new_post1)
    new_post2 = Post(title="Второй пост",
                    message="Привет! это снова я",
                     date_create=datetime.datetime.now(),
                     user_id=new_user1.id,
                    tag_id=new_tag2.id)
    session.add(new_post2)
    new_post3 = Post(title="Первый пост",
                    message="это мой первый пост. Привет!",
                    date_create=datetime.datetime.now(),
                    user_id=new_user2.id,
                    tag_id=new_tag1.id)
    session.add(new_post3)
    new_post4 = Post(title="Первый пост",
                    message="это мой первый пост. Привет!",
                    date_create=datetime.datetime.now(),
                    user_id=new_user3.id,
                    tag_id=new_tag1.id)
    session.add(new_post4)
    session.commit()

    new_comment1 = Comment(message="привет",
                          date_create=datetime.datetime.now(),
                          post_id=new_post1.id,
                          user_id=new_user2.id)
    session.add(new_comment1)

    new_comment2 = Comment(message="привет, Андрей",
                          date_create=datetime.datetime.now(),
                          post_id=new_post2.id,
                          user_id=new_user3.id)
    session.add(new_comment2)
    session.commit()
    session.close()