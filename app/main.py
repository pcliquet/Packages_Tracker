from fastapi import FastAPI
from .routers import packages, locations
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(packages.router)
app.include_router(locations.router)
