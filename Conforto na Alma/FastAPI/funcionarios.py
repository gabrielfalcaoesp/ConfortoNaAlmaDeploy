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

class Funcionarios(BaseModel):
    id_funcionario: int
    id_cargo: int
    nome_funcionario: str
    data_nascimento: str
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

@app.get("/Funcionarios/")
async def get_funcionarios():
    query = "SELECT * FROM Funcionarios"
    db_cursor.execute(query)
    funcionarios = db_cursor.fetchall()
    return funcionarios
