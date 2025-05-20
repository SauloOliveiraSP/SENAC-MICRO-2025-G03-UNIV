from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import get_db_connection, init_db

login_router = APIRouter()

init_db()  # Inicializa o banco se não existir

class LoginRequest(BaseModel):
    username: str
    password: str

@login_router.post("/login")
def login(request: LoginRequest):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (request.username, request.password)
    ).fetchone()
    conn.close()

    if user:
        return {"status": "success", "message": "Login realizado com sucesso!"}
    else:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos.")