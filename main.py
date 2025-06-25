from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from ai_engine import generate_response  # import

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request, user_input: str = Form(...)):
    response = generate_response(user_input)
    return templates.TemplateResponse("index.html", {"request": request, "user_input": user_input, "response": response})
