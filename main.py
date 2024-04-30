from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Encomenda(BaseModel):
    id: int
    data_envio: str
    status: str
    destino: str
    peso: float

class LocalizacaoEncomenda(BaseModel):
    id: int
    encomenda_id: int
    data_registro: str
    localizacao: str

encomendas = []
historico_localizacao = []

@app.get("/encomendas/", response_model=List[Encomenda])
async def listar_todas_encomendas():
    return encomendas

@app.post("/encomendas/")
async def criar_encomenda(encomenda: Encomenda):
    encomendas.append(encomenda)
    return {"msg": "Encomenda criada com sucesso!"}

@app.get("/encomendas/{encomenda_id}")
async def ler_encomenda(encomenda_id: int):
    for encomenda in encomendas:
        if encomenda.id == encomenda_id:
            return encomenda
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@app.put("/encomendas/{encomenda_id}")
async def atualizar_encomenda(encomenda_id: int, encomenda: Encomenda):
    for idx, e in enumerate(encomendas):
        if e.id == encomenda_id:
            encomendas[idx] = encomenda
            return {"msg": "Encomenda atualizada com sucesso!"}
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@app.delete("/encomendas/{encomenda_id}")
async def deletar_encomenda(encomenda_id: int):
    for idx, e in enumerate(encomendas):
        if e.id == encomenda_id:
            del encomendas[idx]
            return {"msg": "Encomenda deletada com sucesso!"}
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

@app.post("/encomendas/{encomenda_id}/localizacao", response_model=LocalizacaoEncomenda)
async def adicionar_localizacao_encomenda(encomenda_id: int, localizacao: LocalizacaoEncomenda):
    for enc in encomendas:
        if enc.id == encomenda_id:
            localizacao.encomenda_id = encomenda_id
            historico_localizacao.append(localizacao)
            return {"msg": "Localização da encomenda registrada com sucesso!"}
    raise HTTPException(status_code=404, detail="Encomenda não encontrada")

from fastapi import HTTPException

@app.get("/encomendas/{encomenda_id}/historico_localizacao", response_model=List[LocalizacaoEncomenda])
async def listar_historico_localizacao_encomenda(encomenda_id: int):
    historico = []
    for hist in historico_localizacao:
        if hist.encomenda_id == encomenda_id:
            historico.append(hist)
    if historico:
        return historico
    raise HTTPException(status_code=404, detail="Histórico de localização não encontrado para esta encomenda")

@app.delete("/encomendas/{encomenda_id}/historico_localizacao")
async def limpar_historico_localizacao_encomenda(encomenda_id: int):
    elementos_para_remover = []
    for hist in historico_localizacao:
        if hist.encomenda_id == encomenda_id:
            elementos_para_remover.append(hist)
    for elem in elementos_para_remover:
        historico_localizacao.remove(elem)
    return {"msg": "Histórico de localização da encomenda deletado com sucesso!"}
