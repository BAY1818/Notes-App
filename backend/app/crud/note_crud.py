from sqlalchemy.orm import Session
from ..models.note import Note
from ..schemas.note_schemas import CreateNote, UpdateNote

def note_create(db:Session, note_data:CreateNote):
    new_note = Note(title = note_data.title,
                    content = note_data.content)
    
    db.add(note_data)
    db.commit()
    db.refresh(note_data)
    return note_data

def get_notes(db:Session):
    return db.query(Note).all()

def get_note_id(db:Session):
    return db.query(Note.id).all()


    