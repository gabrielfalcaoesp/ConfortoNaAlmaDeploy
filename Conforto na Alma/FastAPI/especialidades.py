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

class Especialidades(BaseModel):
    id_especialidade: int
    nome_da_especialidade: str

    app = Fastapi()

@app.get("/Especialidades/")
async def get_especialidades():
    query = "SELECT * FROM Especialidades"
    db_cursor.execute(query)
    especialidades = db_cursor.fetchall()
    return especialidades

@app.get("/Especialidades/{id_especialidade}")
async def get_especialidades(id_especialidade: int):
    query = "SELECT * FROM Especialidades WHERE ID = %s"
    values = (id_especialidade)
    db_cursor.execute(query, values)
    especialidades = db_cursor.fetchone()
    if clientes is None:
        raise HTTPException(status_code=404, detail="Especialidade não encontrada")
    return especialidades
