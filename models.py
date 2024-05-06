from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Encomenda(Base):
    __tablename__ = 'encomendas'

    id = Column(Integer, primary_key=True, index=True)
    data_envio = Column(String(255), index=True)  
    status = Column(String(255), index=True)      
    destino = Column(String(255), index=True)     
    peso = Column(Float)

    localizacoes = relationship("LocalizacaoEncomenda", back_populates="encomenda")

class LocalizacaoEncomenda(Base):
    __tablename__ = 'localizacoes_encomenda'

    id = Column(Integer, primary_key=True, index=True)
    encomenda_id = Column(Integer, ForeignKey('encomendas.id'))
    data_registro = Column(String(255), index=True)  
    localizacao = Column(String(255), index=True)    

    encomenda = relationship("Encomenda", back_populates="localizacoes")
