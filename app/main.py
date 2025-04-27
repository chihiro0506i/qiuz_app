import httpx  # ← 追加
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# テンプレート・静的ファイル設定（ここはそのまま）
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# トップページ表示
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# クイズAPI（外部APIから取得版）
@app.get("/api/quizzes")
async def get_quizzes_external():
    url = "https://opentdb.com/api.php?amount=10&type=multiple"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    return data
