from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
import mysql.connector
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import Cliente 
from starlette.staticfiles import StaticFiles
import os
from fastapi.responses import RedirectResponse

from Cliente import router as cliente_router
from consulta import router_consulta as consulta_router
from exame import router_exame as router_exame
from medico import router_medico as router_medico

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="conforto_na_alma",
    autocommit=True
)

db_cursor = db_connection.cursor()


app = FastAPI()
# templates = Jinja2Templates(directory="../HTML") transformar esse template em os.path.dir, refazer deploy, atualizar a pasta e testar 
# app.mount("/CSS", StaticFiles(directory="../CSS"), name="CSS")
# app.mount("/Imagens", StaticFiles(directory="../Imagens"), name="Imagens")
# app.mount("/JS", StaticFiles(directory="../JS"), name="JS")
# app.mount("/Fontes", StaticFiles(directory="../Fontes"), name="Fontes")

# Obter o caminho absoluto do diretório atual do arquivo Python
current_directory = os.path.dirname(os.path.abspath(__file__))

# Definir o caminho para o diretório "Conforto na Alma"
conforto_na_alma_dir = os.path.join(current_directory, "..")

# Definir os caminhos absolutos para os diretórios estáticos
css_dir = os.path.join(conforto_na_alma_dir, "CSS")
imagens_dir = os.path.join(conforto_na_alma_dir, "Imagens")
js_dir = os.path.join(conforto_na_alma_dir, "JS")
fontes_dir = os.path.join(conforto_na_alma_dir, "Fontes")

# Montar as rotas estáticas com os diretórios absolutos
app.mount("/CSS", StaticFiles(directory=css_dir), name="CSS")
app.mount("/Imagens", StaticFiles(directory=imagens_dir), name="Imagens")
app.mount("/JS", StaticFiles(directory=js_dir), name="JS")
app.mount("/Fontes", StaticFiles(directory=fontes_dir), name="Fontes")
html_dir = os.path.join(conforto_na_alma_dir, "HTML")

templates = Jinja2Templates(directory=html_dir)


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

@app.get("/Sobre/")
async def read_hipertrofia( request: Request,):
    return templates.TemplateResponse("Sobre.html", {"request": request})

@app.get("/Unidade/")
async def read_hipertrofia( request: Request,):
    return templates.TemplateResponse("unidade.html", {"request": request})


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

@app.get("/Esqueceu_senha/")
async def read_esqueceusenha( request: Request,):
    return templates.TemplateResponse("recuperar.html", {"request": request})

@app.get("/Agendamento_confirmado/")
async def read_agendamentoconfirmado( request: Request,):
    return templates.TemplateResponse("clienteAgendado.html", {"request": request})

@app.get("/Logout/")
async def logout(request: Request):
    Cliente.boolLogado=""
    Cliente.id_usuario=""
    return RedirectResponse(url="/home/")

@app.get("/Teste/")
async def teste():
    return "message: está funcionando"