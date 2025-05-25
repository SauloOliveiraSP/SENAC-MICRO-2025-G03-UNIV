from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, constr
from service.db import get_db_connection, init_db

register_router = APIRouter()

init_db()  # Inicializa o banco se não existir

class RegisterRequest(BaseModel):
    username: constr(min_length=3)
    password: constr(min_length=4)
    email: EmailStr
    cpf: constr(min_length=11, max_length=14)  # Pode validar melhor se quiser
    cep: constr(min_length=8, max_length=9)    # Também pode validar melhor

@register_router.post("/register")
def register(request: RegisterRequest):
    conn = get_db_connection()

    # Verifica se já existe username ou email
    user_exists = conn.execute(
        "SELECT id FROM users WHERE username = ? OR email = ?",
        (request.username, request.email)
    ).fetchone()

    if user_exists:
        conn.close()
        raise HTTPException(status_code=400, detail="Usuário ou email já cadastrado.")

    # Insere o novo usuário
    conn.execute(
        "INSERT INTO users (username, password, email, cpf, cep) VALUES (?, ?, ?, ?, ?)",
        (request.username, request.password, request.email, request.cpf, request.cep)
    )
    conn.commit()
    conn.close()

    return {"status": "success", "message": "Cadastro realizado com sucesso!"}
