from fastapi import FastAPI
from util.database import init_db
from controller.endereco import router as endereco_router
from controller.pessoa import router as pessoa_router

app = FastAPI(title="FastAPI + SQLModel - MVC + Repository")

init_db()

app.include_router(pessoa_router)
app.include_router(endereco_router)

@app.get("/")
def health():
    return {"status": "ok"}