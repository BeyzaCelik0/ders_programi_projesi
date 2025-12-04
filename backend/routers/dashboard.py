from fastapi import APIRouter, Depends
from .auth import get_current_username

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"],
)


@router.get("/summary")
def get_dashboard_summary(current_username: str = Depends(get_current_username)):
    """
    Kullanıcının rolüne göre genel program özetini döndürür.
    Bu, frontend'in AJAX (fetch) isteğini test etmesi için kullanılır.
    """

    # Basit rol kontrolü(normalde veritabanına sorgu gönderip çekmem lazım)
    if current_username == "admin":
        role = "Sistem Yöneticisi"
        section = "Tüm Fakülte"
    elif current_username == "dean":
        role = "Dekanlık Yetkilisi"
        section = "Mühendislik Fakültesi"
    else:
        role = "Bölüm Yetkilisi"
        section = "Yazılım Mühendisliği"  # Örnek

    return {
        "username": current_username,
        "role": role,
        "section": section,
        "total_courses": 45,
        "unplaced_courses": 3,
        "message": f"{section} için 3 dersin yerleşimi manuel düzenleme gerektiriyor."
    }