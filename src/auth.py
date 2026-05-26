from datetime import timedelta,datetime
from jose import jwt,JWTError
from passlib.context import CryptContext
from config import secret_key,algo,time_to_expire

pwd_context = CryptContext( schemes=["argon2"],deprecated = "auto")

def hash_password(password:str):
    return pwd_context.hash(password)
def verify_password(plain_passwd,hashed_passwd):
    return pwd_context.verify(plain_passwd,hashed_passwd)
def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow()+timedelta(minutes = time_to_expire)
    to_encode.update({"expire":expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode,key=secret_key,algorithm=algo)
    return encoded_jwt
