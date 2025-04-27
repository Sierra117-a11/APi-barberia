# main.py
from fastapi import FastAPI
from config.database import engine, Base
from routes.usuario import router as usuario_router
from routes.contacto import router as contacto_router
from routes.agenda import router as agenda_router
from routes.auth import router as auth_router


app = FastAPI(
    title="API de Barbería",
    description="Gestión de usuarios, agenda, contactos y autenticación",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.include_router(usuario_router, prefix="/api")
app.include_router(contacto_router, prefix="/api")
app.include_router(agenda_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Barbería"}
