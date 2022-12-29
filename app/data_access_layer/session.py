from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

username = "root"
password = "mysql-root-password"
server = "127.0.0.1:3306"
database_name = "PAPER_TRAIL_RECORD_DATA_LOCAL"

SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{username}:{password}@{server}/{database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
