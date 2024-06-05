from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI();

class Cliente(BaseModel):
    nome: str;
    totalGasto: float;
    ocupacao: str;
    qtdePedidos: int;

base_clientes = [];

@app.post("/clientes")
async def clientes(cliente: Cliente):
    base_clientes.append(cliente);
    return cliente;

@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo ao cadastro de clientes!"};

@app.get("/allClientes")
async def root():
    return base_clientes;

@app.get("/clientes/{nome_cliente}")
async def get_cliente(nome_cliente: str):
    for i in base_clientes:
        if i.nome == nome_cliente:
            return i;
    return {"mensagem": "Cliente nao encontrado"};

@app.put("/clientes/{nome_cliente}")
async def update_cliente(nome_cliente: str, cliente: Cliente):
    for i in base_clientes:
        if i.nome == nome_cliente:
            i = cliente;
    return cliente;

@app.put("/clientes/{nome_cliente}")
async def update_cliente(nome_cliente: str, cliente: Cliente):
    for i in base_clientes:
        if i.nome == nome_cliente:
            i = cliente;
    return cliente;


@app.delete("/clientes/{nome_cliente}")
async def delete_cliente(nome_cliente: str):
    for i in base_clientes:
        if i.nome == nome_cliente:
            base_clientes.remove(i);
            return {"message": f"Cliente {i.nome} removido"};
    return {"message": "Cliente não encontrado"};