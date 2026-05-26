from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine
from .config import dburl
engine = create_engine(dburl)
session_local = sessionmaker(bind = engine)

Base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

