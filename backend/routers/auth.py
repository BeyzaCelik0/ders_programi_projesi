from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import schemas, models
from ..database import get_db
from ..utils import verify_password, create_access_token
from ..utils import ACCESS_TOKEN_EXPIRE_MINUTES
from ..utils import get_user_from_token as utils_get_user_from_token

# Router oluşturma
router = APIRouter(
    prefix="",   #içini boşalttım
    tags=["Auth"],
)


# --- Veritabanı İşlemleri ---
def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# --- Token Çözme ve Yetkilendirme Bağımlılığı ---

# Bu, HTTP header'dan token'ı alıp bağımlılıklara iletir.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")


def get_current_username(token: str = Depends(oauth2_scheme)):
    """
    API'ye gelen token'ı alır, utils.py ile çözer ve kullanıcı adını döndürür.
    Başarısız olursa yetkilendirme hatası fırlatır.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token doğrulaması başarısız oldu veya token süresi doldu.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # utils.py'deki fonksiyona devrediyoruz.
    username = utils_get_user_from_token(token)

    if username is None:
        raise credentials_exception

    return username


# ---Endpoints'ler ---

@router.post("/login", response_model=schemas.Token)
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    """Kullanıcı adı ve şifre ile giriş yapar, başarılı ise JWT Token döndürür."""

    user = get_user(db, username=form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Kullanıcı adı veya şifre hatalı.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "is_teacher": user.is_teacher},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", tags=["Users"])
def read_users_me(current_username: str = Depends(get_current_username)):
    """Giriş yapan kullanıcının kim olduğunu test eder."""
    return {"username": current_username, "message": "Yetkilendirme Basarili!"}