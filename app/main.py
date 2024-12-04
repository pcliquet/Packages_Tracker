from fastapi import FastAPI
from routers import encomendas, localizacoes

# Inicializa o app FastAPI
app = FastAPI()

# Inclui os roteadores
app.include_router(encomendas.router)
app.include_router(localizacoes.router)

# from fastapi import FastAPI, HTTPException, Depends
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from database import SessionLocal, engine
# from typing import List
# import models

# # Criar as tabelas no banco de dados
# models.Base.metadata.create_all(bind=engine)

# # Inicializar o FastAPI
# app = FastAPI()

# # Dependência do banco de dados
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Modelos Pydantic
# # class EncomendaBase(BaseModel):
# #     data_envio: str
# #     status: str
# #     destino: str
# #     peso: float

# # class EncomendaCreate(EncomendaBase):
# #     pass

# # class EncomendaResponse(EncomendaBase):
# #     id: int

# #     class Config:
# #         orm_mode = True

# # class LocalizacaoBase(BaseModel):
# #     localizacao: str
# #     data_registro: str

# # class LocalizacaoEncomendaCreate(LocalizacaoBase):
# #     pass

# # class LocalizacaoEncomendaResponse(LocalizacaoBase):
# #     id: int
# #     encomenda_id: int

# #     class Config:
# #         orm_mode = True

# # Endpoints de Encomendas
# @app.get("/encomendas/", response_model=List[EncomendaResponse])
# async def listar_todas_encomendas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     encomendas = db.query(models.Encomenda).offset(skip).limit(limit).all()
#     return encomendas

# @app.get("/encomendas/{encomenda_id}", response_model=EncomendaResponse)
# async def ler_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
#     encomenda = db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()
#     if encomenda:
#         return encomenda
#     raise HTTPException(status_code=404, detail="Encomenda não encontrada")

# @app.post("/encomendas/", response_model=EncomendaResponse)
# async def criar_encomenda(encomenda: EncomendaCreate, db: Session = Depends(get_db)):
#     nova_encomenda = models.Encomenda(
#         data_envio=encomenda.data_envio,
#         status=encomenda.status,
#         destino=encomenda.destino,
#         peso=encomenda.peso
#     )
#     db.add(nova_encomenda)
#     db.commit()
#     db.refresh(nova_encomenda)
#     return nova_encomenda

# @app.put("/encomendas/{encomenda_id}")
# async def atualizar_encomenda(encomenda_id: int, encomenda: EncomendaBase, db: Session = Depends(get_db)):
#     db_encomenda = db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()
#     if db_encomenda:
#         for key, value in encomenda.dict().items():
#             setattr(db_encomenda, key, value)
#         db.commit()
#         db.refresh(db_encomenda)
#         return {"msg": "Encomenda atualizada com sucesso!"}
#     raise HTTPException(status_code=404, detail="Encomenda não encontrada")

# @app.delete("/encomendas/{encomenda_id}")
# async def deletar_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
#     db_encomenda = db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()
#     if db_encomenda:
#         db.delete(db_encomenda)
#         db.commit()
#         return {"msg": "Encomenda deletada com sucesso!"}
#     raise HTTPException(status_code=404, detail="Encomenda não encontrada")

# # Endpoints de Localizações
# @app.post("/encomendas/{encomenda_id}/localizacao", response_model=LocalizacaoEncomendaResponse)
# async def adicionar_localizacao_encomenda(encomenda_id: int, localizacao: LocalizacaoEncomendaCreate, db: Session = Depends(get_db)):
#     db_encomenda = db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()
#     if db_encomenda:
#         db_localizacao = models.LocalizacaoEncomenda(
#             encomenda_id=encomenda_id,
#             localizacao=localizacao.localizacao,
#             data_registro=localizacao.data_registro
#         )
#         db.add(db_localizacao)
#         db.commit()
#         db.refresh(db_localizacao)
#         return db_localizacao
#     raise HTTPException(status_code=404, detail="Encomenda não encontrada")

# @app.get("/encomendas/{encomenda_id}/historico_localizacao", response_model=List[LocalizacaoEncomendaResponse])
# async def listar_historico_localizacao_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
#     historico = db.query(models.LocalizacaoEncomenda).filter(models.LocalizacaoEncomenda.encomenda_id == encomenda_id).all()
#     if historico:
#         return historico
#     raise HTTPException(status_code=404, detail="Histórico de localização não encontrado para esta encomenda")
