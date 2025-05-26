from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.login import login_router
from service.register import register_router

app = FastAPI(
    title="API de Matricula",  # Nome exibido no Swagger
    description="",  # Descrição opcional
    version="1.0.0",                             # Versão da API
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router, tags=["Autenticação"])
app.include_router(register_router, tags=["Cadastro"])
