from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey
from database import Base
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50))
    email = Column(String(150))
    password = Column(String(500))
    role = Column(String(20),default='user')

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    description = Column(String(150))
    qty = Column(Integer)
    price = Column(Float)

class Orders(Base):
    
    __tablename__ = 'order'
    
    id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey(User.id))
    product_id = Column(Integer,ForeignKey(Product.id))
    quantity = Column(Integer)
