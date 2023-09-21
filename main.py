from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from models import Base
from database import engine
from routes.book import book_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(book_router.router)

# 테이블 생성 및 갱신
Base.metadata.create_all(engine)
