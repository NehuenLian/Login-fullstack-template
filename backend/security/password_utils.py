from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_passowrd: str, hashed_passowrd: str) -> bool:
    return pwd_context.verify(plain_passowrd, hashed_passowrd)