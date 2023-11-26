import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
from funcoes import Funcoes
import jwt

# ORM

class FuncionarioDB(db.Base):
    __tablename__ = 'tb_funcionario'
    
    id_funcionario = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    matricula = Column(CHAR(10), nullable=False)
    cpf = Column(CHAR(11), unique=True, nullable=False)
    telefone = Column(CHAR(11), nullable=False)
    grupo = Column(Integer, nullable=False)
    senha = Column(VARCHAR(200), nullable=False)
    
    def __init__(self, id_funcionario, nome, matricula, cpf, telefone, grupo, senha):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.telefone = telefone
        self.grupo = grupo
        self.senha = senha
        
    def check_password(self, password: str) -> bool:
        return password == self.senha
    
    def get_access_token(self) -> str:
        payload = {
            "id_funcionario": self.id_funcionario,
            "nome": self.nome,
            "cpf": self.cpf,
            "grupo": self.grupo,
            "matricula": self.matricula,
            "telefone": self.telefone,
        }
        token = jwt.encode(
            payload,
            "EmainesSecretKey",
            algorithm="HS256",
        )
        return token