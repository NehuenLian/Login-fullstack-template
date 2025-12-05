from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from data_access.database import get_db
from data_access.models import User
from security.password_utils import hash_password
from security.password_utils import verify_password as verify_hashed_password


async def get_user_by_email(db: AsyncSession, email: str):
    statement = select(User).where(User.email == email)
    result = await db.exec(statement)
    user = result.first()

    return user

def verify_password(user: User, input_password: str) -> bool:
    return verify_hashed_password(input_password, user.password)

async def create_user(db: AsyncSession, email: str, password: str):
    hashed_pw = hash_password(password)
    db_user = User(email=email, password=hashed_pw)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user