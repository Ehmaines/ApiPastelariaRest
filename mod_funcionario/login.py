from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from mod_funcionario.LoginBase import Login

import db

from mod_funcionario.FuncionarioModel import FuncionarioDB
router = APIRouter()

@router.post("/login")
def login(corpo: Login):
    try:
        session = db.Session()
        user = session.query(FuncionarioDB).filter_by(cpf=corpo.cpf).first()
        if not user:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        if not user.check_password(corpo.senha):
            print(user)
            raise HTTPException(status_code=401, detail="Senha incorreta")
        return {"access_token": user.get_access_token()}
    except Exception as e:
        print(e)
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

def get_db():
    return SessionLocal()


