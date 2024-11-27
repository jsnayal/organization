# src/database.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from src.constants import databases_path


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


