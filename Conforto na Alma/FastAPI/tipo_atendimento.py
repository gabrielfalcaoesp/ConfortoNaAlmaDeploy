from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class tipo_atendimento(BaseModel):
    id_tipo: int
    nome: str

app = Fastapi()