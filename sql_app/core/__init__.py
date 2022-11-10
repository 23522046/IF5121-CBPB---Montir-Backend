import uvicorn
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sql_app.v1 import schemas
from sql_app.v1.services import crud_user
from sql_app.v1 import models
from sql_app.v1.middleware_user import ACCESS_TOKEN_EXPIRE, authenticate_user, create_access_token, get_current_active_user, get_db
from sql_app.v1.route import Route
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

