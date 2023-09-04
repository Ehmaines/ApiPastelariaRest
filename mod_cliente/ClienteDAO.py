from fastapi import APIRouter
from mod_cliente.Cliente import Cliente

router = APIRouter()
# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/cliente/", tags=["Cliente"])
def get_cliente():
    return {"msg": "get todos executado"}, 200

@router.get("/cliente/{id}", tags=["Cliente"])
def get_cliente(id: int):
    return {"msg": "get um executado"}, 200

@router.post("/cliente/", tags=["Cliente"])
def post_cliente(f: Cliente):
    return {"msg": "post executado", "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone }, 200

@router.put("/cliente/{id}", tags=["Cliente"])
def put_cliente(id: int, f: Cliente):
    return {"msg": "put executado", "id": id, "nome": f.nome, "cpf": f.cpf, "telefone": f.telefone}, 201

@router.delete("/cliente/{id}", tags=["Cliente"])
def delete_cliente(id: int):
    return {"msg": "delete executado"}, 201
