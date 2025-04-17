from fastapi import FastAPI
from api import tables, reservations

app = FastAPI()

app.include_router(tables.router, prefix="/api/v1")
app.include_router(reservations.router, prefix="/api/v1")