from fastapi import APIRouter, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlmodel import Session

from data_access import crud
from data_access.database import get_db
from security.tokens_utils import create_access_token
from validations.schemas import UserLogin, UserRegister
from validations.general_validations import validate_email, validate_password_conditions

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.post("/auth/login")
@limiter.limit("5/minute")
def login(request: Request, user_data: UserLogin, db: Session=Depends(get_db)):

    email_valid = validate_email(user_data.email)
    if not email_valid: 
        raise HTTPException(status_code=400, detail="Invalid email format.")

    user = crud.get_user_by_email(db, user_data.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    validated_password = crud.verify_password(user, user_data.password)
    if not validated_password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub" : user.email})
    return {"access_token" : access_token, "token_type" : "bearer"}


@router.post("/auth/register")
@limiter.limit("3/minute")
def register(request: Request, user_data: UserRegister, db: Session=Depends(get_db)):

    email_valid = validate_email(user_data.email)
    if not email_valid: 
        raise HTTPException(status_code=400, detail="Invalid email format.")
    
    password_valid = validate_password_conditions(user_data.password)
    if not password_valid:
        raise HTTPException(status_code=400, detail="Invalid password format.")

    user_exists = crud.get_user_by_email(db, user_data.email)
    if user_exists:
        raise HTTPException(status_code=409, detail="This email is already in use.")
    
    user_created = crud.create_user(db, user_data.email, user_data.password)
    if not user_created:
        raise HTTPException(status_code=500, detail="Couldn't create account.")
    
    return {"message" : "Account created."}

