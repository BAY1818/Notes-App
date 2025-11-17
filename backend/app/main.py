from fastapi import FastAPI
from .routers.note_router import router as note_router

app = FastAPI()

app.include_router(note_router)

@app.get("/")
def root():
    return {"message":"Notes Api is running"}