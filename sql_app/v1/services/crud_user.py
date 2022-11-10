from sqlalchemy.orm import Session

from sql_app.v1 import schemas
from sql_app.v1 import models
from sql_app.v1 import middleware_user

# User CRUD
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id_user == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = middleware_user.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password, is_active=True, user_type=user.user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user