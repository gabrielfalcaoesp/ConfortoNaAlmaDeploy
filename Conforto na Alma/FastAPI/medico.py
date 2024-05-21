
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

class Medico(BaseModel):
    id_medico: int
    nome: str
    data_de_nascimento: str
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
    numero: int 
    senha: str 
    genero: str 


router_medico = APIRouter()
templates = Jinja2Templates(directory="../HTML")



@router_medico.get("/cadastro/medico")
async def get_cadastro(request: Request):
    return templates.TemplateResponse("cad_funcionario.html", {"request": request})

@router_medico.get("/Medicos/")
async def get_clientes():
    query = "SELECT * FROM Medico"
    db_cursor.execute(query)
    clientes = db_cursor.fetchall()
    return clientes


@router_medico.get("/Medicos/{id_medico}")
async def get_clientes(id_medico: int):
    query = "SELECT * FROM Medico WHERE ID = %s"
    values = (id_medico)
    db_cursor.execute(query, values)
    clientes = db_cursor.fetchone()
    if clientes is None:
        raise HTTPException(status_code=404, detail="Medico não encontrado")
    return clientes

@router_medico.post("/Medicos/Cadastro")
async def create_cliente(
    request: Request,
    nome: str = Form(...),
    data_de_nascimento: str = Form(...),
    crm: str = Form(...),
    unidade: str = Form(...),
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
    query = "INSERT INTO Medico (nome, data_de_nascimento, crm, unidade, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, data_de_nascimento, crm, unidade, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero)
    db_cursor.execute(query, values)
    db_connection.commit()
    return templates.TemplateResponse("funcionarioCadastrado.html", {"request": request})


@router_medico.put("/Medicos/{cliente_id}")
async def update_cliente(cliente_id: int, updated_cliente: Medico):
    query = "UPDATE Medico SET nome = %s, data_de_nascimento = %s, crm = %s, unidade = %s, rg = %s, cpf = %s, email = %s, telefone = %s, cep = %s, estado = %s, cidade = %s, bairro = %s, endereco = %s, numero = %s, senha = %s, genero = %s WHERE ID = %s"
    values = (updated_cliente.nome, updated_cliente.data_de_nascimento, updated_cliente.crm, updated_cliente.unidade, updated_cliente.rg, updated_cliente.cpf, updated_cliente.email, updated_cliente.telefone, updated_cliente.cep, updated_cliente.estado, updated_cliente.cidade, updated_cliente.bairro, updated_cliente.endereco, updated_cliente.numero, updated_cliente.senha, updated_cliente.genero, cliente_id)
    db_cursor.execute(query, values)
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Medico não encontrado")
    db_connection.commit()
    return {"message": "Item atualizado com sucesso"}
    

@router_medico.delete("/Clientes/{cliente_id}")
async def delete_cliente(cliente_id: int):
    query = "DELETE FROM Cliente WHERE id_cliente = %s"
    values = (cliente_id,)
    db_cursor.execute(query, values)
    db_connection.commit()
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"message": "Cliente deletado com sucesso"}

@router_medico.get("/Medicos/Login/")
async def get_funlogin(request: Request,):
    return templates.TemplateResponse("login_funcionario.html", {"request": request})

@router_medico.post("/Medicos/Login")
async def login_cliente(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)):

    query = "SELECT id_medico FROM Medico WHERE email = %s AND senha = %s"
    values = (email, senha)
    db_cursor.execute(query, values)
    usuarioExiste = db_cursor.fetchone()
    if usuarioExiste:
        global boolLogado
        boolLogado = usuarioExiste
        return "Message: Médico cadastrado"
        
    else: 
        return {"message": "Cliente não encontrado"}
    
@router_medico.get("/verificarLogin")
async def verificarLogin():
    global boolLogado
    return boolLogado

@router_medico.get("/Medicos/perfil/")
async def get_medperfil(request: Request,):
    return templates.TemplateResponse("perfil_medico.html", {"request": request})

@router_medico.get("/Medicos/Perfil/")
async def exibirPerfil(request: Request):
    global boolLogado
    if boolLogado == "":
        return "Message: cliente não está logado"
    return templates.TemplateResponse("perfil_medico.html", {"request": request})


@router_medico.post("/Medicos/Perfil/")
async def getInfoCliente():
    global boolLogado
    db_connection.reconnect()
    if boolLogado == "":
        return "Message: médico não está logado"
    else:
        query = "SELECT * FROM medico WHERE id_medico = %s"
        values = (boolLogado)
        db_cursor.execute(query, values)
        infoCliente = db_cursor.fetchone()

        queryAgendamentos = "SELECT * FROM agendamento_consulta WHERE id_medico = %s"
        values = (boolLogado)
        db_cursor.execute(queryAgendamentos, values)
        agendamentosCliente = db_cursor.fetchall()


        queryExames = "SELECT * FROM agendamento_exame WHERE id_medico = %s"
        values = (boolLogado)
        db_cursor.execute(queryExames, values)
        examesCliente = db_cursor.fetchall()

        return infoCliente, agendamentosCliente, examesCliente

