from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    cpf: str
    telefone: str
    compra_fiado: int = None
    dia_fiado: int = None
    senha: str = None