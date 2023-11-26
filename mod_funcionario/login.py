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
        print("14")
        user = session.query(FuncionarioDB).filter_by(cpf=corpo.cpf).first()
        if not user:
            print("16")
            return {"erro": "Usuário ou senha incorretos"}, 400
        if not user.check_password(corpo.senha):
            print(user)
            return {"erro": "Usuário ou senha incorretos"}, 400
        return {"access_token": user.get_access_token()}, 200
    except Exception as e:
        print(e)
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

def get_db():
    return SessionLocal()


