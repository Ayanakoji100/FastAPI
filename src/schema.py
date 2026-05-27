from pydantic import BaseModel,EmailStr

class ProductCreate(BaseModel):
    id:int
    name :str
    description:str
    qty:int
    price:float

class OrderCreate(BaseModel):
    id:int
    product_id:int
    qty:int

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
