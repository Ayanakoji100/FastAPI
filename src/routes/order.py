from fastapi import APIRouter,HTTPException,Depends
from schema import OrderCreate
from sqlalchemy.orm import Session
from model import Orders,Product
from database import get_db
from dependency import get_curr_user

order = APIRouter()

@order.post('/order',tags=['Order'])
async def new_order(order:list[OrderCreate],db:Session = Depends(get_db),user = Depends(get_curr_user)):
    items = {}
    j = 0
    for i in order:
        products = db.query(Product).filter(i.product_id == Product.id).first()
        if not products or (products.qty == 0) or products.qty < i.qty:
            items.update({f'item{j}':"Not available"})
        else:
            products.qty-=i.qty
            items.update({f'item{j}':i.qty})
            new_order = Orders(id = i.id,user_id = user.get('sub'),product_id = i.product_id,quantity = i.qty )
            db.add(new_order)
            db.commit()
        j+=1
    return items