from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class solicitacao_exame(BaseModel):
    id_solicitacao: int
    id_atendimento: int
    id_exame:int

    app = Fastapi()