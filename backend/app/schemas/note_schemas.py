#BaseModel automatically checks,converts and structures data for data validation
from pydantic import BaseModel          
from datetime import datetime

class CreateNote(BaseModel):
    title:str                   #Must write title
    content:str | None = None   #Optional we can leave it empty or write something  

class UpdateNote(BaseModel):
    title:str | None = None
    content: str | None = None

class ResponseNote(BaseModel):
    id : int 
    title : str 
    content : str | None = None   
    created_at : datetime           #checks time 

    class Config:                   
        from_attributes = True      #access for BaseModel 