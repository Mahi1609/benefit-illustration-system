from sqlalchemy import Column, Integer, Float, JSON, DateTime, String, ForeignKey
from datetime import datetime
from .database import Base



class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # ✅ ADD THIS
    input_data = Column(JSON)
    result_data = Column(JSON)
    irr = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)