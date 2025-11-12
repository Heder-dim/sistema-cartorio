from fastapi import FastAPI
from app.database import Base, engine
from app import routes
from fastapi.middleware.cors import CORSMiddleware

# Cria as tabelas no SQLite
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Cartório - API")

# Permitir acesso do front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)

@app.get("/")
def root():
    return {"mensagem": "API do Sistema de Cartório está ativa!"}
