from fastapi import FastAPI
from routes import routes
import uvicorn


app = FastAPI()
app.include_router(routes)

if __name__ == '__main__':
    uvicorn.run("main:app",host = "127.0.0.1",port = 8000,reload=True)