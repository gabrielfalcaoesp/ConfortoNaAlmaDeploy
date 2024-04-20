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

class Medico(BaseModel):
    id_medico: int
    id_cargo: int
    nome: str
    data_nascimento: str
    crm: str
    unidade: str
    rg: str
    cpf: str
    email: str
    telefone: str
    cep: str
    estado: str
    cidade: str
    bairro: str
    endereco: str
    numero: str
    senha: str
    genero: str

    app = Fastapi()

@app.get("/Medico/")
async def get_medico():
    query = "SELECT * FROM Medico"
    db_cursor.execute(query)
    medico = db_cursor.fetchall()
    return medico

@app.get("/Medico/{id_medico}")
async def get_medico(id_medico: int):
    query = "SELECT * FROM Medico WHERE ID = %s"
    values = (id_medico)
    db_cursor.execute(query, values)
    medico = db_cursor.fetchone()
    if medico is None:
        raise HTTPException(status_code=404, detail="Medico não encontrado")
    return medico
