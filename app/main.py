import uvicorn
from fastapi import FastAPI
from api import tables, reservations

app = FastAPI()

app.include_router(tables.router, prefix="/api/v1")
app.include_router(reservations.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
