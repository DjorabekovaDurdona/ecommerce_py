from database import engine, SessionLocal, Base
from models import Author, Post, Category, Tag
from sqlalchemy.orm import joinedload, selectinload

# создать таблицы
# Base.metadata.create_all(bind=engine)


def get_posts_safe():
    db = SessionLocal()

    # ✅ FIX N+1 problem
    posts = (
        db.query(Post)
        .options(
            selectinload(Post.author),
            selectinload(Post.category),
            selectinload(Post.tags)
        )
        .all()
    )

    for post in posts:
        print("TITLE:", post.title)
        print("AUTHOR:", post.author.name)
        print("CATEGORY:", post.category.name)
        print("TAGS:", [t.name for t in post.tags])
        print("-" * 40)

    db.close()


if __name__ == "__main__":
    get_posts_safe()
    