# Module6: User Management API

This is a FastAPI-based user management application that provides user registration, login, and retrieval functionality with JWT authentication and GitHub OAuth integration.

## Features

- User registration and login with JWT token generation
- GitHub OAuth authentication
- Protected endpoints for user data retrieval
- PostgreSQL database integration
- Password hashing with bcrypt
- JWT token-based authentication

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`:
   ```env
   DB_USER=your_db_user
   DB_PASS=your_db_password
   DB_NAME=your_db_name
   JWT_SECRET_KEY=your_jwt_secret_key
   JWT_ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   GITHUB_CLIENT_ID=your_github_client_id
   SECRET=your_github_client_secret
   FRONTEND_URL=http://localhost:5173
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### User Management (`/users`)

- `POST /users/register`: Register a new user
  - Request body: `{"username": "string", "fullname": "string", "email": "string", "password": "string"}`
  - Response: `{"username": "string", "email": "string"}`

- `POST /users/login`: Login and get access token
  - Request body: `{"username": "string", "password": "string"}`
  - Response: `{"message": "Login successful", "username": "string", "access_token": "string", "access_token_type": "bearer"}`

- `GET /users/`: Get all users (requires authentication)
  - Headers: `Authorization: Bearer <access_token>`
  - Response: Array of user objects

### Authentication (`/auth`)

- `GET /auth/github/login`: Initiate GitHub OAuth login
  - Redirects to GitHub authorization page

- `GET /auth/github/callback`: GitHub OAuth callback
  - Exchanges authorization code for access token
  - Creates/updates user account
  - Redirects to frontend with JWT token

## Database Schema

The application uses PostgreSQL with the following User table structure:
- `id`: Primary key (auto-increment)
- `username`: Unique username (max 50 chars)
- `fullname`: User's full name
- `email`: Unique email address (max 100 chars)
- `password_hash`: Hashed password (nullable for OAuth users)
- `github_id`: GitHub user ID (nullable)
- `avatar_url`: GitHub avatar URL (nullable)
- `auth_provider`: Authentication provider ("github" or null)

## Authentication

The API supports two authentication methods:

1. **JWT Token Authentication**: Use `Authorization: Bearer <token>` header
2. **GitHub OAuth**: Redirect-based authentication flow

## Development

To run in development mode with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Access the interactive API documentation at: `http://localhost:8000/docs`