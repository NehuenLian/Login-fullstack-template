from fastapi import APIRouter, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from sqlmodel import Session

import crud
from data_access.database import get_db
from schemas import UserLogin, UserRegister
from security.tokens_utils import create_access_token

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

@router.post("/auth/login")
@limiter.limit("5/minute")
def login(request: Request, user_data: UserLogin, db: Session=Depends(get_db)):
    user = crud.get_user_by_username(db, user_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    validated_password = crud.verify_password(user, user_data.password)
    if not validated_password:
        raise HTTPException(status_code=401, detail="Incorred password")
    
    access_token = create_access_token(data={"sub" : user.username})
    return {"access_token" : access_token, "token_type" : "bearer"}


@router.post("/auth/register")
@limiter.limit("3/minute")
def register(request: Request, user_data: UserRegister, db: Session=Depends(get_db)):
    user_exists = crud.get_user_by_username(db, user_data.username)
    if user_exists:
        return HTTPException(status_code=409, detail="Username already has taken.")
    
    user_created = crud.create_user(db, user_data.username, user_data.password)
    if not user_created:
        return HTTPException(status_code=500, detail="Couldn't create account.")
    
    return {"message" : "Account created."}

