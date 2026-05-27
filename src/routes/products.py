from fastapi import APIRouter,HTTPException,Depends,status
from model import Product
from sqlalchemy.orm import Session
from database import get_db
from dependency import get_curr_user
from schema import ProductCreate
product = APIRouter(prefix='/product')

@product.get('/view',tags = ['product'])
async def view_product(db:Session = Depends(get_db),payload = Depends(get_curr_user)):
    products = db.query(Product).all()
    if not products:
        raise HTTPException(status_code=400,detail="No product Found")
    return products
@product.post('/add',tags = ['product'])
async def view_product(product:ProductCreate,db:Session = Depends(get_db),payload = Depends(get_curr_user)):
    role = payload.get("role")
    if role != "admin":
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail = "Only authorized to admin")
    new_product = Product(id = product.id,name = product.name,description = product.description,qty = product.qty,price = product.price)
    db.add(new_product)
    db.commit()
    return {"Message":"Product added"}

