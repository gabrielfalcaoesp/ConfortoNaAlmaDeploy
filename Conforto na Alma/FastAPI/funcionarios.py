from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class funcionarios(BaseModel):
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