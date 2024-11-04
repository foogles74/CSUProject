from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeMeta

DATABASE_URL = "postgresql://admin:123qwe@127.0.0.1:5432/main"

class DBConnect:
    def __init__(self, database_url: str = DATABASE_URL):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.SessionLocal()

Base: DeclarativeMeta = declarative_base()