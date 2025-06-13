from fastapi import APIRouter, HTTPException, Depends
from typing import List, Annotated
from dto.user import UserRequest, UserResponse
import models.user
from database import  SessionLocal
from sqlalchemy.orm import  Session

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/", response_model=List[UserResponse])
def read_users(db: db_dependency):
    users = db.query(models.user.User).all()
    return users

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: db_dependency):
    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
