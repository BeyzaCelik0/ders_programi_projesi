from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi.security import OAuth2PasswordBearer

# Modelleri ve Veritabanı altyapısını import ettik.
from . import models
from .database import engine

# Router'ları import ediyoruz
from .routers.auth import router as auth_router
from .routers.users import router as users_router
from .routers import auth, users, dashboard

# Veritabanı tablolarını (User ve Course) oluşturduk.
models.Base.metadata.create_all(bind=engine)

# FastAPI uygulamasını başlattık.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

app = FastAPI(
    title="Ders Programı API",
    description="Ders programı yönetimi için FastAPI Backend",
    version="1.0.0",
    # Swagger'da 'Authorize' butonu için ekledik
    openapi_extra={
        "components": {
            "securitySchemes": {
                "OAuth2PasswordBearer": {
                    "type": "oauth2",
                    "flows": {
                        "password": {
                            "tokenUrl": "/api/login",
                            "scopes": {}
                        }
                    }
                }
            }
        },
        "security": [{"OAuth2PasswordBearer": []}]
    }
)

#Router'ı uygulamaya dahil ediyoruz.
app.include_router(auth_router, prefix="/api")   #değiştirdim
app.include_router(users_router, prefix="/api")

app.include_router(dashboard.router)

app.mount("/frontend", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/")
def read_root():
    """API'nin çalışıp çalışmadığını kontrol ediyoruz."""
    return {"message": "Ders Programı API'si çalışıyor"}

# Uygulamayı başlatmak için bu bloğu kullanacağız
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)