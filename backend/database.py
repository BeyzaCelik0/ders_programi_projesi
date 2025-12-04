from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# PostgreSQL veritabanının bağlantı dizesi
DATABASE_URL = "postgresql://postgres:Beyza12345.@localhost:5432/ders_programi_db"

# SQLAlchemy motorunu oluşturma
engine = create_engine(
    DATABASE_URL
)

# Her veritabanı işleminde kullanılacak SessionLocal sınıfı
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı modelleri için temel sınıf
Base = declarative_base()

# Bağımlılık fonksiyonu: API uç noktaları tarafından kullanılacaktır.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()