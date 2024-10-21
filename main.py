from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="API da Digital College Brasil",
    description="API da Digital College Brasil, feita para fazer requisições em itens do Sponte e coletar dados de maneira eficiente.",
    version="1.0.0",
)

# Simulação de banco de dados em memória
fake_db = []

# Definir um modelo para os dados
class Item(BaseModel):
    name: str
    description: str

# Rota para obter todos os itens
@app.get("/items", response_model=List[Item], summary="Obter todos os itens", response_description="Lista de itens")
def get_items():
    """
    Obter todos os itens armazenados.
    Retorna uma lista de itens.
    """
    return fake_db

# Rota para criar um novo item
@app.post("/items", response_model=Item, summary="Criar um novo item", response_description="Item criado")
def create_item(item: Item):
    """
    Criar um novo item.
    Recebe um item e o armazena na lista.
    """
    fake_db.append(item)
    return item
