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

class Exame(BaseModel):
    id_exame: int
    nome_exame: str

    app = Fastapi()

@app.get("/Exame/")
async def get_exame():
    query = "SELECT * FROM Exame"
    db_cursor.execute(query)
    exame = db_cursor.fetchall()
    return exame

@app.get("/Exame/{id_exame}")
async def get_exame(id_exame: int):
    query = "SELECT * FROM Exame WHERE ID = %s"
    values = (id_exame)
    db_cursor.execute(query, values)
    Exame = db_cursor.fetchone()
    if Exame is None:
        raise HTTPException(status_code=404, detail="Exame não encontrado")
    return Exame