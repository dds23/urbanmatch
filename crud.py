from sqlalchemy.orm import Session
import models
import schemas
from fastapi import HTTPException
from sqlalchemy import func


def create_user(user: schemas.UserCreate, gender: str, gender_preference: str, db: Session):
    db_user = db.query(models.User).filter(
        models.User.email == user.email).first()
    if db_user is not None:
        raise HTTPException(status_code=409, detail="User already exists")
    db_user = models.User(**user.model_dump(), gender=gender,
                          gender_preference=gender_preference)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(skip, limit, db: Session):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users


def get_user(user_id, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(user_id, user: schemas.UserUpdate, db: Session):
    db_user = get_user(user_id, db)
    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    db_user = get_user(user_id, db)
    db.delete(db_user)
    db.commit()
    return {f'User with id {user_id} deleted'}


def find_matches(user_id: int, db: Session):
    db_user = get_user(user_id, db)
    matches = db.query(models.User).filter(
        models.User.id != db_user.id,
        models.User.gender == db_user.gender_preference,
        models.User.city == db_user.city,
        models.User.interests.op('&&')(db_user.interests)
    ).all()
    return matches
