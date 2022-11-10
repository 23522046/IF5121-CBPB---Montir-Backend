from fastapi import Depends
from sqlalchemy.orm import Session
from sql_app.v1 import schemas
from sql_app.v1 import models

def create_vehicle(db: Session, vehicle: schemas.VehicleCreate, user: models.User):
    db_vehicle = models.Vehicle(no_kendaraan= vehicle.no_kendaraan, id_user= user.id_user)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

# filter by id_user
def get_vehicles(db: Session, id_user: int, skip: int=0, limit: int=100):
    return db.query(models.Vehicle).filter(models.Vehicle.id_user == id_user).offset(skip).limit(limit).all()