from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = "root"
password = "mysql-root-password"
server = "localhost:3306"
database_name = "PAPER_TRAIL_RECORD_DATA_LOCAL"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{username}:{password}@{server}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
