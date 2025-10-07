import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL, 
                       connect_args={"check_same_thread" : False},
                       echo=True)

def get_db():
    with Session(engine) as session:
        yield session