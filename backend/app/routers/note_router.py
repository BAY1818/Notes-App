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

@router.get("/",response_model=list[ResponseNote])
def read_notes(db:Session = Depends(get_db)):
    return get_notes(db)

@router.get("/{note_id}",response_model=ResponseNote)
def read_note(db:Session = Depends(get_db), note_id = int):
    note = get_note_id(db,note_id)
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    return note

@router.put("/{node_id}",response_model=ResponseNote)
def update_note(note_data:UpdateNote, note_id = int, db:Session = Depends(get_db)):
    note = note_update(db,note_id,note_data)
    if not note:
        raise HTTPException(status_code=404,detail="Note not found")
    return note

@router.delete("/{note_id}",response_model=ResponseNote)
def delete_note(note_id:int, db:Session = Depends(get_db)):
    result = note_delete(db,note_id)
    if not result:
        raise HTTPException(status_code=404,detail = "Note not found")
    return {"message":"Note Deleted"}