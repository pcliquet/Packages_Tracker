from pydantic import BaseModel
from typing import List, Optional

class EncomendaBase(BaseModel):
    data_envio: str
    status: str
    destino: str
    peso: float

class EncomendaCreate(EncomendaBase):
    pass

class EncomendaUpdate(BaseModel):
    data_envio: Optional[str] = None
    status: Optional[str] = None
    destino: Optional[str] = None
    peso: Optional[float] = None

class EncomendaResponse(EncomendaBase):
    id: int
    class Config:
        orm_mode = True

class LocalizacaoBase(BaseModel):
    localizacao: str
    data_registro: str

class LocalizacaoEncomendaCreate(LocalizacaoBase):
    pass

class LocalizacaoEncomendaResponse(LocalizacaoBase):
    id: int
    encomenda_id: int
    class Config:
        orm_mode = True
