# routes/usuario.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from controllers.usuario import create_usuario, delete_usuario, get_usuarios, update_usuario
from schemas.usuario import UsuarioCreate, UsuarioUpdate, Usuario

router = APIRouter(
    tags=["Usuarios"]  # Añade el tag "Usuarios"
)

@router.post("/usuarios/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario(db, usuario)

@router.get("/usuarios/", response_model=list[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    return get_usuarios(db)

@router.put("/usuarios/{usuario_id}", response_model=Usuario)
def actualizar_usuario(
    usuario_id: int, usuario_data: UsuarioUpdate, db: Session = Depends(get_db)
):
    updated_usuario = update_usuario(db, usuario_id, usuario_data)
    if not updated_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated_usuario

@router.delete("/usuarios/{usuario_id}", response_model=dict)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    success = delete_usuario(db, usuario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"detail": "Usuario eliminado correctamente"}