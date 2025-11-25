from fastapi import Header, HTTPException, status
from typing import Optional
from jose import jwt, JWTError
from app.config import settings


class AuthUser:
    """Authenticated user information."""
    def __init__(self, user_id: str, role: str = "user", email: Optional[str] = None):
        self.user_id = user_id
        self.role = role
        self.email = email


async def get_current_user(authorization: Optional[str] = Header(None)) -> AuthUser:
    """
    Extract and validate JWT token from Authorization header.
    In DEV_MODE, accepts format: "Bearer <user_id>" for testing.
    In production, validates actual JWT tokens from Supabase.
    """
    
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Extract token from "Bearer <token>" format
    parts = authorization.split()
    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format. Expected: Bearer <token>",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    token = parts[1]
    
    # Development mode: accept simple user_id as token
    if settings.DEV_MODE:
        return AuthUser(user_id=token, role="user")
    
    # Production mode: validate JWT token
    try:
        # Decode JWT token (Supabase JWT)
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        
        user_id: str = payload.get("sub")
        email: str = payload.get("email")
        role: str = payload.get("role", "user")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return AuthUser(user_id=user_id, role=role, email=email)
        
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Could not validate credentials: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
