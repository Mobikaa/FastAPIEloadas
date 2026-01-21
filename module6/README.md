# Module6: User Management API

This is a FastAPI-based user management application that provides user registration, login, and retrieval functionality with JWT authentication.

## Features

- User registration
- User login with JWT token generation
- Protected endpoints for user data retrieval
- PostgreSQL database integration

## Setup

1. Create a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```
   pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv python-jose[cryptography] passlib[bcrypt]
   ```

3. Set up environment variables in `.env`:
   ```
   DB_USER=your_db_user
   DB_PASS=your_db_password
   DB_NAME=your_db_name
   ```

4. Run the application:
   ```
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /users/register`: Register a new user
- `POST /users/login`: Login and get access token
- `GET /users/`: Get all users (requires authentication)