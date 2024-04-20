from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

templates_dir = os.path.join(os.path.dirname(__file__), "Template")
templates = Jinja2Templates(directory=templates_dir)

app = FastAPI()

@app.get("/")
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/DSA")
def read_dsa():
    return "DSA"

@app.get("/LLD")
def read_lld():
    return "LLD"

@app.get("/HLD")
def read_hld():
    return "HLD"

@app.get("/SQL")
def read_sql():
    return "SQL"

@app.get("/Languages")
def read_languages():
    return "Languages"

@app.get("/Data-Engineering")
def read_data_engineering():
    return "Data Engineering"