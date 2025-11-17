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

def get_note_id(db:Session, note_id : int):
    return db.query(Note).filter(Note.id == note_id).first()

def note_update(db:Session, note_id : int, note_data:UpdateNote):
    note = get_note_id(db,note_id)
    if not note:
        return None
    
    if note_data.title is not None:
        note.title = note_data.title
    if note_data.content is not None:
        note.content = note_data.content

    db.refresh()
    db.commit() 




    