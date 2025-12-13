import asyncio
import os
from sqlmodel import SQLModel, Field
from sqlalchemy.ext.asyncio import create_async_engine

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    role: str = "user"

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "test.db")
DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

engine = create_async_engine(DATABASE_URL, echo=True)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
