from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class especialidades(BaseModel):
    id_especialidade: int
    nome_da_especialidade: str