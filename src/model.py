from sqlalchemy import Column,Integer,String,Float,Date
from database import Base
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50))
    email = Column(String(150))
    password = Column(String(500))