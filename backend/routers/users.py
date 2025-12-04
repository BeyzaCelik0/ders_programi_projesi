from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db

from .auth import get_current_username

# Router oluşturma
router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# --- Endpoint'ler ---

@router.get("", response_model=List[schemas.UserBase])
def read_users(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        # Yetki kontrolü için get_current_username bağımlılığını kullanıyoruz
        current_username: str = Depends(get_current_username)
):
    """Tüm kullanıcıları listeler. (Yetki gerektirir)"""

    # Kullanıcı yetkilendirildiğine göre, tüm kullanıcıları listele
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users