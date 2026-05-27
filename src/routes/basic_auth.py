from schema import usercreate,userlogin,token
from jose import jwt,JWTError
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from config import secret_key,algo
from database import get_db
from model import User
from auth import hash_password,create_access_token,verify_password
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from dependency import get_curr_user #,get_admin_token
auth = APIRouter()

# oauth2cheme = OAuth2PasswordBearer(tokenUrl='login')

@auth.post('/register',tags =["Auth"])
async def register(user:usercreate,db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400,detail = "User already Exists")
    new_user = User( id = user.id,username = user.username,email = user.email,password = hash_password(user.password))
    db.add(new_user)
    db.commit()
    #db.refresh(new_user)
    return {
        "Message":"User Created Successfully"
    }
@auth.post('/login',response_model=token,tags =["Auth"])
async def login(user:OAuth2PasswordRequestForm =Depends(),db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if not existing_user:
        raise HTTPException(status_code=400,detail = "user doesn't exists")
    if not verify_password(user.password,existing_user.password):
        raise HTTPException(status_code=400,detail = "Incorrect credentials")
    access_token = create_access_token({"sub":existing_user.id,"role":existing_user.role})
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }    
@auth.get('/user',tags =["Auth"])
async def get_user(payload = Depends(get_curr_user),db:Session = Depends(get_db)):
    try:
        # payload = jwt.decode(token=token,key=secret_key,algorithms=[algo])
        username = payload.get("sub")
        user = db.query(User).filter(User.id == username).first()
        if not user:
            raise HTTPException(status_code=404,detail="User not found")
        return user
    except JWTError:
        HTTPException(status_code=401,detail = "Invalid token")
    