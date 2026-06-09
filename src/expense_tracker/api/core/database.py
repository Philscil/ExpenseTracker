from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# The SQLite database file will be saved in the root of the project
SQLALCHEMY_DATABASE_URL = "sqlite:///.expenses.db"

engine = create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This is a factory that gives the Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All of our future database models will inherit from this Base class
Base = declarative_base()

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()