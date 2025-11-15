from sqlalchemy.orm import sessionmaker, declarative_base
from .database import engine


# Create a session factory 
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine )


# Base Class for all models
Base = declarative_base()

# Dependency for FastAPI routes 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
