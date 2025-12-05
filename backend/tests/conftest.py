import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.pool import StaticPool

from data_access.database import get_db
from main import app

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

async_engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
    )

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@pytest_asyncio.fixture(scope="session")
async def prepare_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

@pytest_asyncio.fixture
async def db_session(prepare_db):
    async with async_session() as session:
        yield session
        
@pytest_asyncio.fixture
async def client(db_session):
    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
