from sqlalchemy.orm import Session
from sqlalchemy import update
from sql_app.v1 import schemas
from sql_app.v1 import models

# complete overwrite
def set_booking(db: Session, booking: schemas.Booking, user: models.User):
    if booking.id_booking == None:
        # create new data
        db_booking = models.Booking(id_customer=user.id_user, id_vehicle=booking.id_vehicle, lat_customer=booking.lat_customer, lng_customer=booking.lng_customer, status="processed")
        db.add(db_booking)
    else:
        # complete overwrite
        db_booking = db.query(models.Booking).filter(models.Booking.id_booking == booking.id_booking)
        db_booking.update(
            {
                "id_customer": booking.id_customer,
                "id_montir": booking.id_montir,
                "id_vehicle": booking.id_vehicle,
                "lat_customer": booking.lat_customer,
                "lng_customer": booking.lng_customer,
                "lat_montir": booking.lat_montir,
                "lng_montir": booking.lng_montir,
                "status": booking.status},synchronize_session="fetch")
    
    db.commit()
    db.refresh(db_booking)
    return db_booking

# update parsial
def update_booking(db: Session, id_booking: int, user: models.User, new_data: dict):
    db_booking = db.query(models.Booking).filter(models.Booking.id_booking == id_booking)
    db_booking.update(new_data, synchronize_session="fetch")
    db.commit()
    db_booking = db_booking.first()
    db.refresh(db_booking)
    return db_booking
