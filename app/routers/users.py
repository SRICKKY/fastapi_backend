from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from dependencies.auth import create_access_token, get_current_user
from dependencies.db import get_db
from models.user import User

router = APIRouter()

# Endpoint for user login
@router.post("/login", response_model=dict)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, 
        expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint for user logout
@router.post("/logout", response_model=dict)
async def logout(current_user: User = Depends(get_current_user)):
    # Your logout logic here
    return {"message": "Logout successful"}

# Example protected endpoint that requires a valid access token
@router.get("/protected")
async def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": "This is a protected route"}

