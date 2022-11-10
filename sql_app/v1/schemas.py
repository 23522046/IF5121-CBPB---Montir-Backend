from pydantic import BaseModel

class ProfilBase(BaseModel):
    nama: str
    alamat: str
    telepon: str
    picture: str | None = None

class ProfilCreate(ProfilBase):
    pass

class Profil(ProfilBase):
    id_user: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    user_type: str

class User(UserBase):
    id_user: int
    is_active: bool
    hashed_password: str
    # profil: Profil

    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    lat_customer: float
    lng_customer: float
    id_vehicle: int

class BookingCreate(BookingBase):
    id_booking: int | None = None
    lat_montir: float | None = None
    lng_montir: float | None = None
    status: str | None = None

class BookingUpdate(BaseModel):
    id_booking: int
    lat_montir: float
    lng_montir: float

class Booking(BookingBase):
    id_booking: int
    id_customer: int
    id_montir: int | None = None
    lat_montir: float
    lng_montir: float
    status: str

    class Config:
        orm_mode = True

class VehicleBase(BaseModel):
    no_kendaraan: str
    
# atribut harus sesuai format body raw, jika kosong, maka lihat ke atribut parent class
class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    id_vehicle: int
    id_user: int
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
