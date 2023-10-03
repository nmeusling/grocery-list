from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import get_db
from app.db.base_class import Base


@pytest.fixture(scope="session", autouse=True)
def db():
    SQLALCHEMY_DATABASE_URL = "sqlite://"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    client = TestClient(app)
    yield client
