from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

# --- 1. Kullanıcı Veri Modelleri ---

# Kullanıcı veritabanından çekildiğinde kullanılacak temel model
class UserBase(BaseModel):
    username: str
    is_teacher: bool
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True # Veritabanı objelerini modele dönüştürmeyi sağlar.
    )

# Kullanıcı oluşturulurken gelen veriyi tanımlayan model
class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

# Veritabanından dönen tüm kullanıcı bilgileri modeli
class UserInDB(UserBase):
    id: int
    created_at: datetime

# --- 2. Token Modelleri ---

# Login için API'ye POST ile gelecek veri
class UserLogin(BaseModel):
    username: str
    password: str

# API'den Dönen JWT Token'ın yapısını tanımlar.
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# JWT içindeki kullanıcı bilgisini tanımlar.
class TokenData(BaseModel):
    username: Optional[str] = None
    is_teacher: Optional[bool] = None

# --- 3. Ders Modelleri (Course) ---

class Course(BaseModel):
    id: int
    name: str
    code: str

    model_config = ConfigDict(
        from_attributes=True
    )