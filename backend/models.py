from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


# Veritabanındaki Users tablosu
class User(Base):
    __tablename__ = "users"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Kullanıcı adı ve şifre
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)
    is_teacher = Column(Boolean, default=False)  # Rol yönetimi

    # Kayıt tarihi
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(username='{self.username}', is_teacher={self.is_teacher})>"


# Course tablosu
class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    code = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Course(name='{self.name}', code='{self.code}')>"