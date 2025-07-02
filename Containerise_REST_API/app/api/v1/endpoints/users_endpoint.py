from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserRead
from app.db.session import SessionLocal
from app.crud import user_crud as crud_user
import logging

logger = logging.getLogger("fastapi_app")

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    logger.debug(f"Received user creation request: {user}")
    created_user = crud_user.create_user(db, user)
    logger.info(f"User created with ID: {created_user.id}")
    return created_user

@router.get("/", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    logger.debug("Fetching all users")
    users = crud_user.get_users(db)
    logger.info(f"Retrieved {len(users)} users")
    return users

@router.get("/{user_id}", response_model=UserRead)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Fetching user with ID: {user_id}")
    user = crud_user.get_user_by_id(db, user_id)
    if not user:
        logger.warning(f"User with ID {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update(user_id: int, user_in: UserCreate, db: Session = Depends(get_db)):
    logger.debug(f"Updating user ID {user_id} with data: {user_in}")
    user = crud_user.update_user(db, user_id, user_in)
    if not user:
        logger.warning(f"Update failed: User with ID {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"User with ID {user_id} updated")
    return user

@router.delete("/{user_id}", status_code=204)
def delete(user_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Attempting to delete user with ID {user_id}")
    success = crud_user.delete_user(db, user_id)
    if not success:
        logger.error(f"Deletion failed: User with ID {user_id} not found")
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"User with ID {user_id} deleted successfully")