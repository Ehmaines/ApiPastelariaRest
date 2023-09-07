from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import STR_DATABASE

engine = create_engine(STR_DATABASE)
Session = sessionmaker(bind=engine)
# para trabalhar com tabelas
Base = declarative_base()

def criaTabelas():
    Base.metadata.create_all(engine)