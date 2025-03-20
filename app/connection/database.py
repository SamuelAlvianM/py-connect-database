from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv('.env')

Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Using database URL: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)
print(f"data: {engine}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Error creating database tables: {e}")

def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()