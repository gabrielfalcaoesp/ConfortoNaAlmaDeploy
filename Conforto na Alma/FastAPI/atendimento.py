from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class atendimento(BaseModel):
    id_atendimento: int
    id_cliente: int
    id_medico: int
    data_agendamento: str
    data_agendada: str
    horario_consulta: str
    prescricao: str
    resultado: int
    id_especialidade: int
    id_tipo: int