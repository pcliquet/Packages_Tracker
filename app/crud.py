from sqlalchemy.orm import Session
import models, schemas

def listar_encomendas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Encomenda).offset(skip).limit(limit).all()

def criar_encomenda(db: Session, encomenda: schemas.EncomendaCreate):
    nova_encomenda = models.Encomenda(
        data_envio=encomenda.data_envio,
        status=encomenda.status,
        destino=encomenda.destino,
        peso=encomenda.peso
    )
    db.add(nova_encomenda)
    db.commit()
    db.refresh(nova_encomenda)
    return nova_encomenda

def ler_encomenda(db: Session, encomenda_id: int):
    return db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()

def atualizar_encomenda(db: Session, encomenda_id: int, encomenda: schemas.EncomendaUpdate):
    db_encomenda = db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()
    if not db_encomenda:
        return None
    for key, value in encomenda.dict(exclude_unset=True).items():
        setattr(db_encomenda, key, value)
    db.commit()
    db.refresh(db_encomenda)
    return db_encomenda

def deletar_encomenda(db: Session, encomenda_id: int):
    db_encomenda = db.query(models.Encomenda).filter(models.Encomenda.id == encomenda_id).first()
    if not db_encomenda:
        return False
    db.delete(db_encomenda)
    db.commit()
    return True

def criar_localizacao_encomenda(db: Session, encomenda_id: int, localizacao: schemas.LocalizacaoEncomendaCreate):
    nova_localizacao = models.LocalizacaoEncomenda(
        encomenda_id=encomenda_id,
        localizacao=localizacao.localizacao,
        data_registro=localizacao.data_registro
    )
    db.add(nova_localizacao)
    db.commit()
    db.refresh(nova_localizacao)
    return nova_localizacao

def listar_historico_localizacoes(db: Session, encomenda_id: int):
    return db.query(models.LocalizacaoEncomenda).filter(models.LocalizacaoEncomenda.encomenda_id == encomenda_id).all()
