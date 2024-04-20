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

class Cargo(BaseModel):
    id_cargo: int
    cargo: str

    app = Fastapi()

@app.get("/Cargo/")
async def get_cargo():
    query = "SELECT * FROM Cargo"
    db_cursor.execute(query)
    cargo = db_cursor.fetchall()
    return cargo

