from sqlmodel import Session, select

from data_access.database import get_db
from data_access.models import User
from security.password_utils import hash_password
from security.password_utils import verify_password as verify_hashed_password


def get_user_by_email(db: Session, email: str):
    statement = select(User).where(User.email == email)
    user = db.exec(statement).first()
    return user

def verify_password(user: User, input_password: str) -> bool:
    return verify_hashed_password(input_password, user.password)

def create_user(db: Session, email: str, password: str):
    hashed_pw = hash_password(password)
    db_user = User(email=email, password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user