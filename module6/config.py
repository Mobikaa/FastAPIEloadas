import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "")
SECRET = os.getenv("SECRET", "")
GITHUB_REDIRECT_URI = "http://localhost:8000/auth/github/callback"

FRONTEND_URL = os.getenv("FRONTEND_URL")