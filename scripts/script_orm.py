from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Projeto(Base):
    __tablename__ = 'projetos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    lider = Column(String)
    atividades = relationship("Atividade", back_populates="projeto")


class Atividade(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    projeto_id = Column(Integer, ForeignKey('projetos.id'))
    descricao = Column(String)
    projeto = relationship("Projeto", back_populates="atividades")


# Conexão ao banco de dados
engine = create_engine('postgresql://user:password@localhost/AtividadesBD')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Inserir uma atividade
nova_atividade = Atividade(projeto_id=1, descricao='Nova Atividade')
session.add(nova_atividade)

# Atualizar o líder de um projeto
projeto = session.query(Projeto).filter_by(id=1).first()
projeto.lider = 'Novo Líder'

# Listar todos os projetos e suas atividades
projetos = session.query(Projeto).all()
for projeto in projetos:
    print(projeto.nome, projeto.lider)
    for atividade in projeto.atividades:
        print(f"  - {atividade.descricao}")

session.commit()
session.close()
