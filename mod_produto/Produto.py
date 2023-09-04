from pydantic import BaseModel

class Produto(BaseModel):
    id_cliente: int = None
    nome: str
    descricao: str
    foto: str = None
    valor_unitario: int