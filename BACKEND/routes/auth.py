# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.usuario import get_usuario_by_correo
from schemas.usuario import UsuarioCreate
from config.database import get_db

router = APIRouter(
    tags=["Autenticación"]  # Añade el tag "Autenticación"
)

@router.post("/login")
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = get_usuario_by_correo(db, correo=usuario.correo)
    if not db_usuario or db_usuario.contraseña != usuario.contraseña:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"mensaje": "Inicio de sesión exitoso"}