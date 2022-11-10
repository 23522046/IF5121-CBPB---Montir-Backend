# for migrate scheme

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = "users"
    
    id_user = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    user_type = Column(String, nullable=False)
    
    # user_profil = relationship("Profil", back_populates="profil_user")
    # montir_booking = relationship("Booking", back_populates="booking_montir")
    # customer_booking = relationship("Booking", back_populates="customer_montir")

class Profil(Base):
    __tablename__ = "profiles"

    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False, primary_key=True)
    nama = Column(String, index=True, nullable=False)
    alamat = Column(String)
    telepon = Column(String, index=True, nullable=False)
    picture = Column(String)
    

    # profil_user = relationship("User", back_populates="user_profil")

class Vehicle(Base):
    __tablename__ = "vehicles"
    id_vehicle = Column(Integer, primary_key=True, index=True)
    no_kendaraan = Column(String)
    id_user = Column(Integer, ForeignKey("users.id_user"))


class Booking(Base):
    __tablename__ = "bookings"

    id_booking = Column(Integer, primary_key=True, index=True)
    id_customer = Column(Integer, ForeignKey("users.id_user"), nullable=False)
    id_montir = Column(Integer, ForeignKey("users.id_user"), nullable=True)
    id_vehicle = Column(Integer, ForeignKey("vehicles.id_vehicle"), nullable=False)
    lat_customer = Column(Float, nullable=False)
    lng_customer = Column(Float, nullable=False)
    lat_montir = Column(Float, default=0, nullable=True)
    lng_montir = Column(Float, default=0, nullable=True)
    status = Column(String, index=True, nullable=False, default="proses")

    # booking_montir = relationship("User", back_populates="montir_booking")
    # booking_customer = relationship("User", back_populates="customer_booking")

