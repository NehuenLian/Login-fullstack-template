import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from data_access.database import get_db
from main import app


@pytest.fixture
def client():

    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread" : False},
        poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)

    def get_test_db():
        session = Session(engine)
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = get_test_db

    return TestClient(app)