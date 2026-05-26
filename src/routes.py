from .schema import usercreate,userlogin,token
from jose import jwt,JWTError
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .config import secret_key,algo
from .database import get_db
from .model import User
from .auth import hash_password,create_access_token,verify_password
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
routes = APIRouter()

oauth2cheme = OAuth2PasswordBearer(tokenUrl='login')

@routes.post('/register')
async def register(user:usercreate,db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(user.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400,detail = "User already Exists")
    new_user = User( username = User.username,email = User.email,password = hash_password(User.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "Message":"User Created Successfully"
    }
@routes.post('/login',response_model=token)
async def login(user:userlogin,db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(user.username == user.username).first()
    if not existing_user:
        raise HTTPException(status_code=400,detail = "user doesn't exists")
    if not verify_password(user.password,existing_user.password):
        raise HTTPException(status_code=400,detail = "Incorrect credentials")
    access_token = create_access_token({"sub":existing_user.username})
    return {
        "access_token":access_token,
        "token_type":"jwt"
    }    
@routes.get('/user')
async def get_user(token:str = Depends(oauth2cheme)):
    try:
        payload = jwt.decode(token=token,key=secret_key,algorithms=[algo])
        username = payload.get("set")
        return {"Message":f'Hello {username}'}
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")
    