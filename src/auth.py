# src/auth.py
import jwt
from datetime import datetime, timedelta
from .constants import SECRET_KEY, ALGORITHM

def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Create a JWT token with the provided data and expiration time.
    """
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_access_token(token: str):
    """
    Decode and verify the JWT token.
    """
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_data
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
