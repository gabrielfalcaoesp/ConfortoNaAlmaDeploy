from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="Clinica" #Confirmar nome da database depois 
)
db_cursor = db_connection.cursor()

class Atendimento(BaseModel):
    id_atendimento: int
    id_cliente: int
    id_medico: int
    data_agendamento: str
    data_agendada: str
    horario_consulta: str
    prescricao: str
    resultado: int
    id_especialidade: int
    id_tipo: int

    app = Fastapi()

@app.get("/Atendimento/")
async def get_atendimento():
    query = "SELECT * FROM Atendimento"
    db_cursor.execute(query)
    atendimento = db_cursor.fetchall()
    return atendimento

@app.get("/Atendimento/{id_atendimento}")
async def get_atendimento(id_atendimento: int):
    query = "SELECT * FROM Atendimento WHERE ID = %s"
    values = (id_atendimento)
    db_cursor.execute(query, values)
    atendimento = db_cursor.fetchone()
    if atendimento is None:
        raise HTTPException(status_code=404, detail="Erro")
    return atendimento
