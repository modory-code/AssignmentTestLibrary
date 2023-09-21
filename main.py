from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from models import Base
from database import engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def home():
    return {"message": "Hello World!"}

# 테이블 생성 및 갱신
Base.metadata.create_all(engine)
