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

@app.get("/")
async def read_index( request: Request,):
    return templates.TemplateResponse("index.html", {"request": request})

