
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./app.db"     # Sqlite Database URL


engine = create_engine(         # Create the SQLAlachemy engine
    DATABASE_URL,
    connect_args={"check_same_thread": False}      # Required for SQLite
)