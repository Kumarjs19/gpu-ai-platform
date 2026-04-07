from sqlalchemy import Column, String, Integer, DateTime
from api.db import Base
import uuid, datetime

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True)
    password = Column(String)
    credits = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Job(Base):
    __tablename__ = "jobs"
    id = Column(String, primary_key=True)
    user_id = Column(String)
    type = Column(String)
    prompt = Column(String)
    status = Column(String)
    result = Column(String)
