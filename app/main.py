from fastapi import FastAPI
from routers import encomendas, localizacoes

app = FastAPI()

app.include_router(encomendas.router)
app.include_router(localizacoes.router)