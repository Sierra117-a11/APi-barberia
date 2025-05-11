# routes/agenda.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from controllers.agenda import (
    obtener_agendas, crear_agenda, actualizar_agenda, eliminar_agenda, agendas_semana
)
from schemas.agenda import AgendaCreate, Agenda

router = APIRouter(
    tags=["Agendas"]  # Añade el tag "Agendas"
)

@router.get("/agenda", response_model=List[Agenda])
def listar_agendas(db: Session = Depends(get_db)):
    return obtener_agendas(db)

@router.post("/agenda")
def crear_nueva_agenda(agenda: AgendaCreate, db: Session = Depends(get_db)):
    return crear_agenda(db, agenda)

@router.put("/agenda/{id}")
def actualizar_agenda_existente(id: int, agenda: AgendaCreate, db: Session = Depends(get_db)):
    updated_agenda = actualizar_agenda(db, id, agenda)
    if not updated_agenda:
        raise HTTPException(status_code=404, detail="Agenda no encontrada")
    return {"msg": "Agenda actualizada"}

@router.delete("/agenda/{id}")
def eliminar_agenda_existente(id: int, db: Session = Depends(get_db)):
    success = eliminar_agenda(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Agenda no encontrada")
    return {"msg": "Agenda eliminada"}

@router.get("/agenda/calendario")
def ver_calendario_semanal(db: Session = Depends(get_db)):
    return agendas_semana(db)