import uvicorn
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from sql_app.v1 import schemas
from sql_app.v1.services import crud_user, crud_vehicle, crud_booking
from sql_app.v1.middleware_user import ACCESS_TOKEN_EXPIRE, authenticate_user, create_access_token, get_current_user, get_current_active_user, get_db, oauth_scheme
from sql_app.v1.route import Route
from sql_app.core import app

@app.post(Route.TOKEN, response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    # print('here')
    # print(f'hashed pwd : {get_password_hash(form_data.password)}')
    user = authenticate_user(form_data.username, form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get(Route.USERS_ME, response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_active_user)):
    print(current_user)
    return current_user

@app.post(Route.USERS, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email aready taken")
    return crud_user.create_user(db=db, user=user)

@app.get(f"{Route.USERS}user_id", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth_scheme)):
    db_user = crud_user.get_user_by_id(db, user_id=user_id)
    if db_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

# Endpoint vehicle
@app.post('/users/vehicles', response_model=schemas.Vehicle)
def create_user_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    db_vehicle = crud_vehicle.create_vehicle(db, vehicle=vehicle, user=user)
    return db_vehicle

@app.get('/users/vehicles', response_model=list[schemas.Vehicle])
def get_user_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    vehicles = crud_vehicle.get_vehicles(db, id_user=user.id_user, skip=skip, limit=limit)
    return vehicles

# Endpoint booking
@app.post('/users/booking', response_model=schemas.Booking)
def get_user_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    b = schemas.BookingCreate(id_customer=user.id_user, id_vehicle=booking.id_vehicle, lat_customer=booking.lat_customer, lng_customer=booking.lng_customer)
    db_booking = crud_booking.set_booking(db, booking=b, user=user)
    return db_booking

# method ini dijalankan oleh montir only
@app.post('/users/booking/assign-montir', response_model=schemas.Booking)    
def assign_montir(booking: schemas.BookingUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    updated_data = {"id_montir": user.id_user, "lat_montir": booking.lat_montir, "lng_montir": booking.lng_montir, "status": "confirmed"}
    db_booking = crud_booking.update_booking(db, id_booking=booking.id_booking, user=user, new_data=updated_data)
    return db_booking

@app.post('/users/booking/update-lokasi-montir', response_model=schemas.Booking)    
def assign_montir(booking: schemas.BookingUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    updated_data = {"lat_montir": booking.lat_montir, "lng_montir": booking.lng_montir}
    db_booking = crud_booking.update_booking(db, id_booking=booking.id_booking, user=user, new_data=updated_data)
    return db_booking