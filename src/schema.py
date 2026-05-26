from pydantic import BaseModel,EmailStr

class usercreate(BaseModel):
    id:int
    username:str
    email:EmailStr
    password:str
class userlogin(BaseModel):
    username:str
    password:str
class token(BaseModel):
    access_token:str
    token_type:str
