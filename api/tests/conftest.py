import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from config import user_test, password_test, host_test, db_name_test
from main import app
from models import Base
from database import get_session


TEST_DATABASE_URL = f'postgresql://{user_test}:{password_test}@{host_test}/{db_name_test}'


@pytest.fixture(scope='session')
def create_test_database():
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope='session')
def test_session(create_test_database):
    engine = create_engine(TEST_DATABASE_URL)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture
def client(test_session):
    def override_get_session():
        return test_session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as client:
        yield client
