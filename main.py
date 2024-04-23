from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Encomenda(BaseModel):
    id: int
    # cliente_id: int -> Caso seja necessario integraçao com cliente.
    data_envio: str
    status: str
    destino: str
    peso: float

encomendas = [

]

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
    return {"msg": "Encomenda não encontrada"}

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
