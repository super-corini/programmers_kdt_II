import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'weapon.db')
SQLALCHEMY_DATABASE_URL = f"sqlite:///{dbfile}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()