from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from ai_engine import get_response

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):
    reply = get_response(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "user_input": user_input, "reply": reply})
