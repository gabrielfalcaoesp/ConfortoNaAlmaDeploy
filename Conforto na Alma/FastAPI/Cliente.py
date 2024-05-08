from fastapi import FastAPI, HTTPException, Form
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

boolLogado = False

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


app = FastAPI()
templates = Jinja2Templates(directory="../HTML")
app.mount("/CSS", StaticFiles(directory="../CSS"), name="CSS")
app.mount("/Imagens", StaticFiles(directory="../Imagens"), name="Imagens")
app.mount("/JS", StaticFiles(directory="../JS"), name="JS")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitações de qualquer origem
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir métodos HTTP
    allow_headers=["*"],  # Permitir cabeçalhos personalizados
)



@app.get("/Clientes/")
async def get_clientes():
    query = "SELECT * FROM Clientes"
    db_cursor.execute(query)
    clientes = db_cursor.fetchall()
    return clientes


@app.get("/Clientes/{id_cliente}")
async def get_clientes(id_cliente: int):
    query = "SELECT * FROM Clientes WHERE ID = %s"
    values = (id_cliente)
    db_cursor.execute(query, values)
    clientes = db_cursor.fetchone()
    if clientes is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return clientes


@app.post("/Clientes/Cadastro")
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
    query = "INSERT INTO Clientes (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, data_de_nascimento, rg, cpf, email, telefone, cep, estado, cidade, bairro, endereco, numero, senha, genero)
    db_cursor.execute(query, values)
    db_connection.commit()
    return templates.TemplateResponse("clienteCadastrado.html", {"request": request})


@app.put("/Clientes/{cliente_id}")
async def update_cliente(cliente_id: int, updated_cliente: Cliente):
    query = "UPDATE Clientes SET nome = %s, data_de_nascimento = %s, rg = %s, cpf = %s, email = %s, telefone = %s, cep = %s, estado = %s, cidade = %s, bairro = %s, endereco = %s, numero = %s, senha = %s, genero = %s WHERE ID = %s"
    values = (updated_cliente.nome, updated_cliente.data_de_nascimento, updated_cliente.rg, updated_cliente.cpf, updated_cliente.email, updated_cliente.telefone, updated_cliente.cep, updated_cliente.estado, updated_cliente.cidade, updated_cliente.bairro, updated_cliente.endereco, updated_cliente.numero, updated_cliente.senha, updated_cliente.genero, cliente_id)
    db_cursor.execute(query, values)
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db_connection.commit()
    return {"message": "Item atualizado com sucesso"}
    

@app.delete("/Clientes/{cliente_id}")
async def delete_cliente(cliente_id: int):
    query = "DELETE FROM Clientes WHERE id_cliente = %s"
    values = (cliente_id,)
    db_cursor.execute(query, values)
    db_connection.commit()
    if db_cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"message": "Cliente deletado com sucesso"}

@app.post("/Clientes/Login")
async def login_cliente(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...)):

    query = "SELECT * FROM Clientes WHERE email = %s AND senha = %s"
    values = (email, senha)
    db_cursor.execute(query, values)
    usuarioExiste = db_cursor.fetchone()
    db_cursor.close()
    if usuarioExiste:
        global boolLogado
        boolLogado = True
        return templates.TemplateResponse("index.html", {"request": request, "boolLogado": boolLogado})
        
    else: 
        return {"message": "Cliente não encontrado"}
    
@app.get("/verificarLogin")
async def verificarLogin():
    global boolLogado
    return boolLogado

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


