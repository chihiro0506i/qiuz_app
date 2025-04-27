from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from . import models, database, schemas
import random

app = FastAPI()

# CORSミドルウェア（省略可，もし問題なければそのまま）
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# テンプレートと静的ファイル設定
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# DBテーブル作成
models.Base.metadata.create_all(bind=database.engine)


# DBセッション
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# トップページ（/）をindex.htmlで返す
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# クイズデータAPI
@app.get("/api/quizzes", response_model=schemas.QuizListResponse)
def get_quizzes(db: Session = Depends(get_db)):
    quizzes = db.query(models.Quiz).all()
    selected = random.sample(quizzes, k=10)
    return {"quizzes": selected}
