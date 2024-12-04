from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas
from typing import List

router = APIRouter(prefix="/encomendas", tags=["Encomendas"])

@router.get("/", response_model=List[schemas.EncomendaResponse])
async def listar_todas_encomendas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lista todas as encomendas com paginação.
    """
    return crud.listar_encomendas(db, skip, limit)

@router.post("/", response_model=schemas.EncomendaResponse)
async def criar_encomenda(encomenda: schemas.EncomendaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova encomenda.
    """
    return crud.criar_encomenda(db, encomenda)

@router.get("/{encomenda_id}", response_model=schemas.EncomendaResponse)
async def ler_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    """
    Retorna os detalhes de uma encomenda pelo ID.
    """
    encomenda = crud.ler_encomenda(db, encomenda_id)
    if not encomenda:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return encomenda

@router.put("/{encomenda_id}", response_model=schemas.EncomendaResponse)
async def atualizar_encomenda(encomenda_id: int, encomenda: schemas.EncomendaUpdate, db: Session = Depends(get_db)):
    """
    Atualiza uma encomenda existente pelo ID.
    """
    encomenda_atualizada = crud.atualizar_encomenda(db, encomenda_id, encomenda)
    if not encomenda_atualizada:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return encomenda_atualizada

@router.delete("/{encomenda_id}")
async def deletar_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    """
    Deleta uma encomenda pelo ID.
    """
    sucesso = crud.deletar_encomenda(db, encomenda_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return {"msg": "Encomenda deletada com sucesso!"}

