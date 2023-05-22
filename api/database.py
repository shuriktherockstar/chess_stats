from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import user, password, host, db_name

DATABASE_URL = f'postgresql://{user}:{password}@{host}/{db_name}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
