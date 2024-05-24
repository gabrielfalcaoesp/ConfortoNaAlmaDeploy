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
