from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Encomenda, LocalizacaoEncomenda
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from typing import List

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Cria as tabelas no banco de dados se não existirem

# Dependência para obter a sessão do SQLAlchemy
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelos Pydantic para validação de entrada
class EncomendaModel(BaseModel):
    id: int
    data_envio: str
    status: str
    destino: str
    peso: float

class LocalizacaoEncomendaModel(BaseModel):
    id: int
    encomenda_id: int
    data_registro: str
    localizacao: str

# Rotas adaptadas para usar o banco de dados
@app.post("/encomendas/", response_model=EncomendaModel)
async def criar_encomenda(encomenda: EncomendaModel, db: Session = Depends(get_db)):
    db_encomenda = Encomenda(**encomenda.dict())
    db.add(db_encomenda)
    db.commit()
    db.refresh(db_encomenda)
    return db_encomenda

@app.get("/encomendas/", response_model=List[EncomendaModel])
async def listar_todas_encomendas(db: Session = Depends(get_db)):
    encomendas = db.query(Encomenda).all()
    return encomendas

@app.get("/encomendas/{encomenda_id}", response_model=EncomendaModel)
async def ler_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    encomenda = db.query(Encomenda).filter(Encomenda.id == encomenda_id).first()
    if encomenda is None:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return encomenda

@app.put("/encomendas/{encomenda_id}", response_model=EncomendaModel)
async def atualizar_encomenda(encomenda_id: int, encomenda: EncomendaModel, db: Session = Depends(get_db)):
    db_encomenda = db.query(Encomenda).filter(Encomenda.id == encomenda_id).first()
    if db_encomenda is None:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    for var, value in vars(encomenda).items():
        setattr(db_encomenda, var, value) if value else None
    db.commit()
    return db_encomenda

@app.delete("/encomendas/{encomenda_id}")
async def deletar_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    db_encomenda = db.query(Encomenda).filter(Encomenda.id == encomenda_id).first()
    if db_encomenda is None:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    db.delete(db_encomenda)
    db.commit()
    return {"msg": "Encomenda deletada com sucesso!"}

@app.post("/encomendas/{encomenda_id}/localizacao", response_model=LocalizacaoEncomendaModel)
async def adicionar_localizacao_encomenda(encomenda_id: int, localizacao: LocalizacaoEncomendaModel, db: Session = Depends(get_db)):
    db_localizacao = LocalizacaoEncomenda(**localizacao.dict(), encomenda_id=encomenda_id)
    db.add(db_localizacao)
    db.commit()
    db.refresh(db_localizacao)
    return db_localizacao

@app.get("/encomendas/{encomenda_id}/historico_localizacao", response_model=List[LocalizacaoEncomendaModel])
async def listar_historico_localizacao_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    historico = db.query(LocalizacaoEncomenda).filter(LocalizacaoEncomenda.encomenda_id == encomenda_id).all()
    return historico

@app.delete("/encomendas/{encomenda_id}/historico_localizacao")
async def limpar_historico_localizacao_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    db.query(LocalizacaoEncomenda).filter(LocalizacaoEncomenda.encomenda_id == encomenda_id).delete()
    db.commit()
    return {"msg": "Histórico de localização da encomenda deletado com sucesso!"}
