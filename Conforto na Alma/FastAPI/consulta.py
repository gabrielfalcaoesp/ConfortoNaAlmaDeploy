from fastapi import FastAPI, HTTPException, Form, APIRouter
import fastapi
from pydantic import BaseModel
import mysql.connector
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


db_connection = mysql.connector.connect(
    host="server-cna.mysql.database.azure.com",
    user="gabriel",
    password="senai103@",
    database="conforto_na_alma" 
)
db_cursor = db_connection.cursor()

class Consulta(BaseModel):
    id_cliente: int
    id_medico: int
    tipo_consulta: str
    data_agendada: str
    data_agendamento: str
    horario_consulta: str
    unidade: str

router_consulta = APIRouter()
router_consulta.mount("/CSS", StaticFiles(directory="../CSS"), name="CSS")
router_consulta.mount("/Imagens", StaticFiles(directory="../Imagens"), name="Imagens")
templates = Jinja2Templates(directory="../HTML")



@router_consulta.get("/Agendamento/")
async def get_agendamentos(request: Request):
    return templates.TemplateResponse("agendamento.html", {"request": request})


@router_consulta.get("/Agendamento/Especialidade")
async def get_especialidade(request: Request):
    return templates.TemplateResponse("agendamento_especialidade.html", {"request": request})

@router_consulta.get("/Agendamento/Data")
async def get_data(request: Request):
    return templates.TemplateResponse("agendamento_data.html", {"request": request})

@router_consulta.get("/Agendamento/Profissional")
async def get_profissional(request: Request):
    return templates.TemplateResponse("agendamento_profissional.html", {"request": request})

@router_consulta.get("/Agendamento/Confirmacao")
async def get_profissional(request: Request):
    return templates.TemplateResponse("agendamento_confirmacao.html", {"request": request})


@router_consulta.get("/Agendamento/pagamento/{metodo_pagamento}")
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

@router_consulta.post("/Agendamento/Enviar")
async def enviar_agendamento(request: Request, consulta: Consulta):
    query = "INSERT INTO agendamento_consulta (id_cliente, id_medico, tipo_consulta, data_agendada, data_agendamento, horario_consulta, unidade) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (consulta.id_cliente, consulta.id_medico, consulta.tipo_consulta, consulta.data_agendada, consulta.data_agendamento, consulta.horario_consulta, consulta.unidade)
    db_cursor.execute(query, values)
    db_connection.commit()
    return templates.TemplateResponse("index.html", {"request": request})

@router_consulta.get("/Detalhes/Consulta/")
async def get_detalhes(request: Request):
    return templates.TemplateResponse("agendamento_detalhes.html", {"request": request})

@router_consulta.get("/Desmarcar/Consulta/{agendamentoDelete}")
async def get_detalhes(request: Request):
    return templates.TemplateResponse("Confirmacao_DesmarcarAgendamento.html", {"request": request})

@router_consulta.post("/Deletar/Consulta/{agendamentoDelete}")
async def deletar_consulta(request: Request, agendamentoDelete: int):
    try:
        query = "DELETE FROM agendamento_consulta WHERE id_agendamento_consulta = %s"
        values = (agendamentoDelete,)  # Note a vírgula para criar uma tupla
        db_cursor.execute(query, values)
        db_connection.commit()
        return {"message": "Consulta deletada com sucesso"}
    except Exception as e:
        # Em caso de erro, retornar uma resposta de erro
        return {"error": str(e)}
