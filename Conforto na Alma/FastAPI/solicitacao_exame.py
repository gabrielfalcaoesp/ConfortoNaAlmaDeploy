from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import mysql.connector


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="conforto_na_alma",
)
db_cursor = db_connection.cursor()

class Solicitacao_exame(BaseModel):
    id_solicitacao: int
    id_atendimento: int
    id_exame:int

    app = Fastapi()

@app.get("/Solicitacao_exame/")
async def get_solicitacao_exame():
    query = "SELECT * FROM Solicitacao_exame"
    db_cursor.execute(query)
    solicitacao_exame = db_cursor.fetchall()
    return solicitacao_exame

@app.get("/Solicitacao_exame/{id_solicitacao}")
async def get_solicitacao_exame(id_solicitacao: int):
    query = "SELECT * FROM Solicitacao_exame WHERE ID = %s"
    values = (id_solicitacao)
    db_cursor.execute(query, values)
    solicitacao_exame = db_cursor.fetchone()
    if solicitacao_exame is None:
        raise HTTPException(status_code=404, detail="Erro")
    return solicitacao_exame
