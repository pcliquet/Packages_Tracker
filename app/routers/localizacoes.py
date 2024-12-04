from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import schemas
import crud

# Inicializar o roteador
router = APIRouter(prefix="/encomendas", tags=["Localizacao"])

@router.post("/{encomenda_id}/localizacao", response_model=schemas.LocalizacaoEncomendaResponse)
async def adicionar_localizacao_encomenda(encomenda_id: int, localizacao: schemas.LocalizacaoEncomendaCreate, db: Session = Depends(get_db)):
    """
    Adiciona uma localização a uma encomenda.
    """
    encomenda = crud.ler_encomenda(db, encomenda_id)
    if not encomenda:
        raise HTTPException(status_code=404, detail="Encomenda não encontrada")
    return crud.criar_localizacao_encomenda(db, encomenda_id, localizacao)

@router.get("/{encomenda_id}/historico_localizacao", response_model=List[schemas.LocalizacaoEncomendaResponse])
async def listar_historico_localizacao_encomenda(encomenda_id: int, db: Session = Depends(get_db)):
    """
    Lista o histórico de localizações de uma encomenda.
    """
    historico = crud.listar_historico_localizacoes(db, encomenda_id)
    if not historico:
        raise HTTPException(status_code=404, detail="Histórico de localização não encontrado para esta encomenda")
    return historico
