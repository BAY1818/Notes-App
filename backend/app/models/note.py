from sqlalchemy import Column,Integer,String,Text,DataTime
from sqlalchemy.sql import func 
from ..db.session import Base

#Note derived class for create table for database 
class Note(Base):
    __tablename__ = "Note"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text,nullable=True)
    created_at = Column(DataTime(timezone = True), server_default=func.now())