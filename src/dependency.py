from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from config import secret_key, algo

oauth2scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_curr_user(token: str = Depends(oauth2scheme)):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algo])
        return payload   
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
