from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class medico(BaseModel):
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