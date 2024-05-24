from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import mysql.connector


db_connection = mysql.connector.connect(
    host="server-cna.mysql.database.azure.com",
    user="gabriel",
    password="senai103@",
    database="conforto_na_alma" 
)
db_cursor = db_connection.cursor()

class Tipo_atendimento(BaseModel):
    id_tipo: int
    nome: str

app = Fastapi()

@app.get("/Tipo_atendimento/")
async def get_tipo_atendimento():
    query = "SELECT * FROM Tipo_atendimento"
    db_cursor.execute(query)
    tipo_atendimento = db_cursor.fetchall()
    return tipo_atendimento

@app.get("/Tipo_atendimento/{id_tipo}")
async def get_tipo_atendimento(id_tipo: int):
    query = "SELECT * FROM Tipo_atendimento WHERE ID = %s"
    values = (id_tipo)
    db_cursor.execute(query, values)
    tipo_atendimento = db_cursor.fetchone()
    if tipo_atendimento is None:
        raise HTTPException(status_code=404, detail="Erro")
    return tipo_atendimento
