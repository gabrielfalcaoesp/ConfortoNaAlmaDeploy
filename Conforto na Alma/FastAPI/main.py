from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import mysql.connector
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from Cliente import router as cliente_router
from consulta import router_consulta as consulta_router
from exame import router_exame as router_exame
from medico import router_medico as router_medico

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="conforto_na_alma" 
)
db_cursor = db_connection.cursor()


app = FastAPI()
templates = Jinja2Templates(directory="../HTML")
app.mount("/CSS", StaticFiles(directory="../CSS"), name="CSS")
app.mount("/Imagens", StaticFiles(directory="../Imagens"), name="Imagens")
app.mount("/JS", StaticFiles(directory="../JS"), name="JS")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitações de qualquer origem
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir métodos HTTP
    allow_headers=["*"],  # Permitir cabeçalhos personalizados
)


app.include_router(cliente_router)
app.include_router(consulta_router)
app.include_router(router_exame)
app.include_router(router_medico)

@app.get("/")
async def read_index( request: Request,):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home/")
async def read_index( request: Request,):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/Hipertrofia/")
async def read_hipertrofia( request: Request,):
    return templates.TemplateResponse("Hipertrofia.html", {"request": request})

@app.get("/Emagrecimento/")
async def read_emagrecimento( request: Request,):
    return templates.TemplateResponse("emagrecimento.html", {"request": request})

@app.get("/Geral/")
async def read_geral( request: Request,):
    return templates.TemplateResponse("geral.html", {"request": request})

@app.get("/Materna/")
async def read_materna( request: Request,):
    return templates.TemplateResponse("materna.html", {"request": request})

@app.get("/Esportiva/")
async def read_esportiva( request: Request,):
    return templates.TemplateResponse("esportiva.html", {"request": request})