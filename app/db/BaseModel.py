from sqlalchemy import Column, String
import uuid

from app.db.DBConnect import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()