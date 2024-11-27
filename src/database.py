# src/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
databases_path = os.path.join(os.path.expanduser('~'), "databases")
if not os.path.exists(databases_path):
    os.mkdir(databases_path)
SQLALCHEMY_DATABASE_URL = f"sqlite:///{databases_path}/master_db.db"  # Replace with your DB

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
