from fastapi import APIRouter
import db
from mod_produto.Produto import Produto
from mod_produto.ProdutoModel import ProdutoDB
from fastapi import Depends
import security

router = APIRouter(dependencies=[Depends(security.verify_token), Depends(security.verify_key)])
# Criar as rotas/endpoints: GET, POST, PUT, DELETE
@router.get("/produto/", tags=["Produto"])
def get_produto():
    try:
        session = db.Session()
        dados = session.query(ProdutoDB).all();
    
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    
    finally:
        session.close()

@router.get("/produto/{id}", tags=["Produto"])
def get_produto(id: int):
    try:
        session = db.Session()
        print("Teste")
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id);
    
        return dados, 200
    
    except Exception as e:
        return {"erro": str(e)}, 400
    
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(p: Produto):
    try:
        session = db.Session()
        dados = ProdutoDB(p.id_produto, p.nome, p.descricao, p.foto, p.valor_unitario)

        session.add(dados)
        session.commit()
        
        return {"id": p.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    
    finally:
        session.close()
        
#Eduardo Heiden Maines

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, p: Produto):
    try:
        session = db.Session()
        print("tranquilo")
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one();
        dados.nome = p.nome
        dados.descricao = p.descricao
        dados.foto = p.foto
        print("tranquilo Passou da foto")
        dados.valor_unitario = p.valor_unitario
    
        session.add(dados)
        session.commit()
    
        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int):
    try:
        session = db.Session()
        
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()
        
        return {"id": dados.id_produto}, 200
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

