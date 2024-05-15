from fastapi import FastAPI, HTTPException, Form, APIRouter
import fastapi
from pydantic import BaseModel
import mysql.connector
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="conforto_na_alma" 
)
db_cursor = db_connection.cursor()

class Exame(BaseModel):
    id_cliente: int
    id_medico: int
    tipo_exame: str
    data_agendada: str
    data_agendamento: str
    horario_consulta: str
    unidade: str

router_exame = APIRouter()
router_exame.mount("/CSS", StaticFiles(directory="../CSS"), name="CSS")
router_exame.mount("/Imagens", StaticFiles(directory="../Imagens"), name="Imagens")
templates = Jinja2Templates(directory="../HTML")



@router_exame.get("/Exame/")
async def get_agendamentos(request: Request):
    return templates.TemplateResponse("agendamento_exame.html", {"request": request})


@router_exame.get("/Exame/Data/")
async def get_data(request: Request):
    return templates.TemplateResponse("data_exame.html", {"request": request})

@router_exame.get("/Exame/Profissional/")
async def get_profissional(request: Request):
    return templates.TemplateResponse("exame_profissional.html", {"request": request})

@router_exame.get("/Exame/Confirmacao")
async def get_profissional(request: Request):
    return templates.TemplateResponse("exame_confirmacao.html", {"request": request})


@router_exame.get("/Exame/pagamento/{metodo_pagamento}")
async def get_pagamento(request: Request, metodo_pagamento: str):
    if metodo_pagamento == "pix":
        return templates.TemplateResponse("pagamento_pix.html", {"request": request})
    elif metodo_pagamento == "cartao":
        return templates.TemplateResponse("pagamento_cartao.html", {"request": request})
    elif metodo_pagamento == "consulta":
        return templates.TemplateResponse("clienteAgendado.html", {"request": request})
    else:
        # Tratamento para método de pagamento inválido
        return {"message": "Método de pagamento inválido"}

@router_exame.post("/Exame/Enviar")
async def enviar_agendamento(request: Request, consulta: Exame):
    query = "INSERT INTO agendamento_exame (id_cliente, id_medico, tipo_exame, data_agendada, data_agendamento, horario_consulta, unidade) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (consulta.id_cliente, consulta.id_medico, consulta.tipo_exame, consulta.data_agendada, consulta.data_agendamento, consulta.horario_consulta, consulta.unidade)
    db_cursor.execute(query, values)
    db_connection.commit()
    return templates.TemplateResponse("index.html", {"request": request})
