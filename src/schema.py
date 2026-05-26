from pydantic import BaseModel,EmailStr

class usercreate(BaseModel):
    username:str
    email:EmailStr
    password:str
class userlogin(BaseModel):
    username:str
    password:EmailStr
class token(BaseModel):
    access_token:str
    token_type:str
