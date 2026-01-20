""" Load environment variables using dotenv.
Read DB_USER and DB_PASS from .env, with fallback defaults.
Create a connection string:
postgresql://<DB_USER>:<DB_PASS>@localhost/fastapi_week4 """
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.article_comment_onetomany import Base, Article, Comment

load_dotenv()

DB_USER = os.getenv("DB_USER", "default_user")
DB_PASS = os.getenv("DB_PASS", "default_pass")

connection_string = f"postgresql://{DB_USER}:{DB_PASS}@localhost/fastapi_week4"

""" Use create_engine() to initialize a SQLAlchemy engine.
Use Base.metadata.create_all() to create tables. """

engine = create_engine(connection_string)
Base.metadata.create_all(engine)

""" Create a session using sessionmaker.
Create one Article titled "Sample Article".
Create two Comment objects with different content.
Associate the comments with the article using:
article.comments = [comment1, comment2]
Add and commit the article (with comments) to the session. """

Session = sessionmaker(bind=engine)
session = Session()

article = Article(title="Sample Article")
comment1 = Comment(content="This is the first comment.")
comment2 = Comment(content="This is the second comment.")

article.comments = [comment1, comment2]

session.add(article)
session.commit()

session.close()

""" Use a new session to query the first article from the database.
Print:
Article ID
Number of comments
Each comment's ID """

new_session = Session()
first_article = new_session.query(Article).first()

if first_article:
    print(f"Article ID: {first_article.id}")
    print(f"Number of comments: {len(first_article.comments)}")
    for comment in first_article.comments:
        print(f"Comment ID: {comment.id}")

new_session.close()
