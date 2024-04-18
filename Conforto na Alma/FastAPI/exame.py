from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class exame(BaseModel):
    id_exame: int
    nome_exame: str

    app = Fastapi()