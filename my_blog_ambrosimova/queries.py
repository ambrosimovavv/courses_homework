from .db.session import Session
from .models.user import User
from .models.post import Post
from .models.comment import Comment
from .models.tag import Tag

if __name__ == '__main__':
    session = Session()

    # Все посты конкретного пользователя

    user = session.query(User).filter_by(username='Andrew Popov').first()
    posts = session.query(Post).filter_by(user_id=user.id).all()

    print(f"Посты пользователя {user.username}:")
    for post in posts:
        print(f"- {post.title}: {post.message}")

    # Все комментарии к конкретному посту
    post = session.query(Post).first()
    comments = session.query(Comment).filter_by(post_id=post.id).all()

    print(f"Комментарии к посту '{post.title}':")
    for c in comments:
        print(f"- {c.message} от пользователя {c.users.username}")

    # Все посты с конкретным тегом
    tag = session.query(Tag).filter_by(message="первый").first()
    posts_with_tag = session.query(Post).filter_by(tag_id=tag.id).all()

    print(f"Посты с тегом '{tag.message}':")
    for post in posts_with_tag:
        print(f"- {post.title} от {post.users.username}")

    # Посты и комментарии конкретного пользователя

    user = session.query(User).filter_by(username="Alex Ivanov").first()

    for post in user.posts:  # если настроен back_populates='posts'
        print(f"Пост: {post.title}")
        for comment in post.comments:
            print(f"  Комментарий: {comment.message} от {comment.user.username}")

