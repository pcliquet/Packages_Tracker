from fastapi import FastAPI
from routers import encomendas, localizacoes
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(encomendas.router)
app.include_router(localizacoes.router)