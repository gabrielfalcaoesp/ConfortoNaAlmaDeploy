from fastapi import FastAPI, HTTPException, Form, APIRouter
from pydantic import BaseModel
import mysql.connector
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware





db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="conforto_na_alma" 
)
db_cursor = db_connection.cursor()

boolLogado = ""
id_usuario = ""

class Cliente(BaseModel):
    id_cliente: int
    nome: str
    data_de_nascimento: str 
    rg: str 
    cpf: str 
    email: str
    telefone: str 
    cep: str
    estado: str 
    cidade: str 
    bairro: str 
    endereco: str 
    numero: int 
    senha: str 
    genero: str 


router = APIRouter()
templates = Jinja2Templates(directory="../HTML")



@router.get("/cadastro/")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.get("/Clientes/")
async def get_clientes():
    query = "SELECT * FROM Cliente"
    db_cursor.execute(query)
    clientes = db_cursor.fetchall()
    return clientes


@router.get("/Clientes/{id_cliente}")
async def get_clientes(id_cliente: int):
    query = "SELECT * FROM Cliente WHERE ID = %s"
    values = (id_cliente)
    db_cursor.execute(query, values)
    clientes = db_cursor.fetchone()
    if clientes is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return clientes


@router.post("/Clientes/Cadastro")
async def create_cliente(
    request: Request,
    nome: str = Form(...),
    data_de_nascimento: str = Form(...),
    rg: str = Form(...),
    cpf: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cep: str = Form(...),
    estado: str = Form(...),
    cidade: str = Form(...),
    bairro: str = Form(...),
    endereco: str = Form(...),
    numero: str = Form(...),
    senha: str = Form(...),
    genero: str = Form(...),
):
    query = "INSERT INTO Cliente (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero)
    db_cursor.execute(query, values)
    db_connection.commit()
    return templates.TemplateResponse("clienteCadastrado.html", {"request": request})


@router.put("/Clientes/{cliente_id}")
async def update_cliente(cliente_id: int, updated_cliente: Cliente):
    query = "UPDATE Cliente SET nome = %s, data_de_nascimento = %s, rg = %s, cpf = %s, email = %s, telefone = %s, cep = %s, estado = %s, cidade = %s, bairro = %s, endereco = %s, numero = %s, senha = %s, genero = %s WHERE ID = %s"
    values = (updated_cliente.nome, updated_cliente.data_de_nascimento, updated_cliente.rg, updated_cliente.cpf, updated_cliente.email, updated_cliente.telefone, updated_cliente.cep, updated_cliente.estado, updated_cliente.cidade, updated_cliente.bairro, updated_cliente.endereco, updated_cliente.numero, updated_cliente.senha, updated_cliente.genero, cliente_id)
    db_cursor.execute(query, values)
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db_connection.commit()
    return {"message": "Item atualizado com sucesso"}
    

@router.delete("/Clientes/{cliente_id}")
async def delete_cliente(cliente_id: int):
    query = "DELETE FROM Cliente WHERE id_cliente = %s"
    values = (cliente_id,)
    db_cursor.execute(query, values)
    db_connection.commit()
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"message": "Cliente deletado com sucesso"}

@router.post("/Clientes/Login")
async def login_cliente(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)):

    query = "SELECT id_cliente FROM Cliente WHERE email = %s AND senha = %s"
    values = (email, senha)
    db_cursor.execute(query, values)
    usuarioExiste = db_cursor.fetchone()
    if usuarioExiste:
        global boolLogado
        boolLogado = usuarioExiste
        return templates.TemplateResponse("index.html", {"request": request, "boolLogado": boolLogado})
        
    else: 
        return {"message": "Cliente não encontrado"}
    
@router.get("/verificarLogin")
async def verificarLogin():
    global boolLogado
    return boolLogado



