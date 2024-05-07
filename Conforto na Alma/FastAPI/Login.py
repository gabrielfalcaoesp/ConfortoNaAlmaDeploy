from fastapi import FastAPI, HTTPException, Depends, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import mysql.connector
from pydantic import BaseModel

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="Conforto_na_Alma" #Confirmar nome da database depois 
)
db_cursor = db_connection.cursor()


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

# Função para verificar se o cliente existe
def get_cliente(nome: str):
    cursor.execute("SELECT * FROM clientes WHERE nome = %s", (nome,))
    cliente = cursor.fetchone()
    if cliente:
        return cliente

# Função para verificar a senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para autenticar o cliente
def authenticate_cliente(nome: str, senha: str):
    cliente = get_cliente(nome)
    if not cliente or not verify_password(senha, cliente[13]):
        return False
    return cliente

# Rota de login
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    cliente = authenticate_cliente(form_data.username, form_data.password)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nome ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": cliente[0], "token_type": "bearer"}

# Exemplo de rota protegida
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    return {"token": token}