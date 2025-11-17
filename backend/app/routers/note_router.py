from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud.note_crud import(
    note_create,
    get_notes,
    get_note_id,
    note_update,
    note_delete
)
from ..schemas.note_schemas import CreateNote, UpdateNote, ResponseNote
from ..db.session import get_db
router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/",response_model=ResponseNote)
def create_new_note(note_data:CreateNote, db:Session = (Depends(get_db))):
    note = note_create(db,note_data)
    return note