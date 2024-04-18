from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

class cargo(BaseModel):
    id_cargo: int
    cargo: str

    app = Fastapi()