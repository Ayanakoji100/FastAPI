from fastapi import FastAPI
from routes.basic_auth import auth
from routes.order import order
from routes.products import product
import uvicorn


app = FastAPI()
app.include_router(auth)
app.include_router(order)
app.include_router(product)


if __name__ == '__main__':
    uvicorn.run("main:app",host = "127.0.0.1",port = 8000,reload=True)