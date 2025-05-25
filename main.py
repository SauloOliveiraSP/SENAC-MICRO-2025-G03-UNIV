from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.login import login_router
from service.register import register_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router)
app.include_router(register_router)
