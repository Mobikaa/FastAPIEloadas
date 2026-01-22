from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from config import GITHUB_CLIENT_ID, SECRET, GITHUB_REDIRECT_URI, FRONTEND_URL
from database import get_db
from models.user import User
from utils import create_access_token
import requests

router = APIRouter()

client_id = GITHUB_CLIENT_ID
client_secret = SECRET
redirect_uri = GITHUB_REDIRECT_URI

@router.get("/github/login")
def github_login():
    print(GITHUB_CLIENT_ID, SECRET)
    if not GITHUB_CLIENT_ID or not SECRET:
        raise HTTPException(status_code=500, detail="GitHub OAuth credentials are not set")
    else:
        print("GitHub OAuth credentials are set")
        
    scope = "user"  # Adjust scope as required
    github_auth_url = f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    return RedirectResponse(github_auth_url)


@router.get("/github/callback")
def github_callback(request: Request, db: Session = Depends(get_db)):
    # Exchange code for access token
    token_url = "https://github.com/login/oauth/access_token"
    code = request.query_params.get("code")
    print("Authorization code received:", code)
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not provided")
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "redirect_uri": redirect_uri
    }
    
    headers = {"Accept": "application/json"}
    response = requests.post(token_url, data=data, headers=headers)
    response.raise_for_status()
    token_data = response.json()
    access_token = token_data.get("access_token")
    print("Access token obtained:", access_token)
    
    if not access_token:
        raise HTTPException(status_code=400, detail="Failed to obtain access token")
    
    # Fetch user profile
    user_url = "https://api.github.com/user"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_response = requests.get(user_url, headers=headers)
    user_response.raise_for_status()
    user_data = user_response.json()
    print("GitHub user data:", user_data)
    
    github_id = str(user_data["id"])
    username = user_data["login"]
    fullname = user_data.get("name", "")
    avatar_url = user_data.get("avatar_url", "")
    
    # Fetch verified email
    emails_url = "https://api.github.com/user/emails"
    emails_response = requests.get(emails_url, headers=headers)
    emails_response.raise_for_status()
    emails_data = emails_response.json()
    print("GitHub user emails:", emails_data)
    
    verified_email = None
    for email_info in emails_data:
        if email_info.get("primary") and email_info.get("verified"):
            verified_email = email_info["email"]
            break
    
    if not verified_email:
        raise HTTPException(status_code=400, detail="No verified email found")
    
    # Check if user exists by github_id or email
    user = db.query(User).filter((User.github_id == github_id) | (User.email == verified_email)).first()
    
    if user:
        # Update existing user
        user.github_id = github_id
        user.avatar_url = avatar_url
        user.auth_provider = "github"
        if not user.fullname:
            user.fullname = fullname
    else:
        # Create new user
        user = User(
            username=username,
            fullname=fullname,
            email=verified_email,
            password_hash=None,  # No password for OAuth
            github_id=github_id,
            avatar_url=avatar_url,
            auth_provider="github"
        )
        db.add(user)
    
    db.commit()
    db.refresh(user)
    
    # Create JWT
    access_token_jwt = create_access_token(data={"sub": user.username, "email": user.email})
    
    return RedirectResponse(f"{FRONTEND_URL}?token={access_token_jwt}")