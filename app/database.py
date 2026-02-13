from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./linguaai.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#🗄 SQLAlchemy
# Engine ka kaam: DB se actual connection manage karna
# SessionLocal ka kaam: Har request ke liye ek naya DB session banana
Base = declarative_base()
