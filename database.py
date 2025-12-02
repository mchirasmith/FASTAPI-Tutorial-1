from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://postgres:210807@localhost:5432/Chirasmith"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush=False , bind = engine)