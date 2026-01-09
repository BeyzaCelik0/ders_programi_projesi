from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError
from typing import Optional

# JWT ayarları
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Token'ın geçerlilik süresi.

# Şifre Hashing Ayarları
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)

# --- Şifre Fonksiyonları ---

def verify_password(plain_password, hashed_password):
    """Kullanıcının girdiği şifre ile DB'deki hash'i karşılaştırır."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Şifreyi veritabanına kaydetmeden önce hashler."""
    return pwd_context.hash(password)

# --- JWT Token Fonksiyonları ---

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Yeni bir JWT Access Token oluşturur."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_user_from_token(token: str):
    """Verilen token'ı çözer ve içindeki kullanıcı verisini döndürür."""

   

        username: str = payload.get("sub")

        if username is None:
            return None

        return username

    except JWTError:
        return None
